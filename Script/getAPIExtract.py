import configparser
import requests
import json
from datetime import datetime
import mysql.connector
import os
import time
api_url = "https://api.tomorrow.io/v4/weather/forecast"
api_key = "JhXdXXNEQoVnVtRemAcisMjl2djZJEUg"

params = {
    "location": "10.7769,106.7009",
    "timesteps": "1d",
    "apikey": api_key
}



def connect(filename):
     # 1. đọc file dbControl.ini
    db_config = configparser.ConfigParser()
    db_config.read(filename)
    host = db_config.get('mysql', 'host')
    user = db_config.get('mysql', 'user')
    password = db_config.get('mysql', 'password')
    database = db_config.get('mysql', 'database')
    try:
     # 2. kết nối cơ sở dữ liệu 
        cnx = mysql.connector.connect(
            user=user, password=password, host=host, database=database)
        if cnx.is_connected():
            print('Connected to MySQL database')
        return cnx
    except mysql.connector.Error as err:
        with open(file_err, 'a') as file:
                 file.write(f'Error: {str(err)}\n')
        print(err)


def getDataFromAPI():
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        current_date = datetime.now().strftime("%d%m%Y")
        save_directory = r"D:\weather_data_Staging"
        file_name = fr"{save_directory}\{current_date}_weather_forecast.json"
        with open(file_name, "w") as json_file:
            json.dump(response.json(), json_file, indent=4)
        print(f"Dữ liệu đã được lưu vào {file_name}")
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
def countdown(t):
    while t:
        minis, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minis, secs)
        print("\r", timer, end="")
        time.sleep(1)
        t -= 1
    print("\r", '00:00', end="")
    print()
if __name__ == '__main__':
    count=0
    # getDataFromAPI()
    current_date = datetime.now().strftime("%d%m%Y")
    currentdate = datetime.now().strftime("%Y:%m:%d")
    save_directory = r"D:\weather_data_Staging"
    file_name = fr"{save_directory}\{current_date}_weather_forecast.json"
    save_directoryEr = r"D:\error_EXTRACT"
    file_err = fr"{save_directoryEr}\{current_date}_weather_forecast.txt"
    fileconfigs = '\dbconfig\dbControl.ini'
    
    current_dir = os.path.dirname(__file__)+fileconfigs
    print(current_dir)
    while True:
        # 1,2
        conn = connect(current_dir)
        # print(conn)
        #3. Kiểm tra kết nối cơ sở dữ liệu 
        if conn is not None:
            try:
                # 3.1. Ghi log kết nối thành công
                query = "INSERT INTO log (status, note, log_date) VALUES ( %s, %s,%s)"
                insertData = ('CONNECT_DB_SUCCESS', 'connect db control success', datetime.now())
                cursor = conn.cursor()
                cursor.execute(query, insertData)
                                             
                # 4 Lấy dữ liệu từ src_path tại control_data_file_configs mà nguồn bằng 1
                cursor.execute('SELECT src_path FROM control_data_file_configs WHERE id = 1')
                result = cursor.fetchone()
                print(result[0])
                # 5 Kiểm tra kết nối 
                while(True):
                    response = requests.get(result[0])   
                    if response.status_code == 200:
                        # 5.1 ghi dư liệu vào file
                        getDataFromAPI()
                        # 5.2 ghi log thành công
                        insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                        cursor.execute(
                            insert_query, (1, 'EXTRACT_SUCCESS', 'crawl success', fr'{currentdate}'))
                        with open(file_name, 'r') as file:
                            dataforecast = json.load(file)
                        # 5.3 ghi dữ liệu Extract thành công vào control_data_file [status= EXTRACT_SUCCESS]
                        insert_query = "INSERT INTO control_data_file (id_config,name, row_count, status,data_range_from,data_range_to,note,create_at,update_at,create_by,update_by) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                        cursor.execute(insert_query, (1, fr'{current_date}_weather_forecast.json', 6, 'EXTRACT_SUCCESS', dataforecast['timelines']['daily'][
                                    0]['time'], dataforecast['timelines']['daily'][5]['time'], 'crawl', fr'{currentdate}', fr'{currentdate}', 'Nhơn', 'Nhơn'))
                    
                        conn.commit()
                        print("Dữ liệu đã được thêm thành công!")
                        break
                    else :
                        # 5.4 ghi log thất bại
                        insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                        cursor.execute(
                            insert_query, (1, 'CONNECT_SOURCE_FAIL', 'connect source unsuccess', fr'{currentdate}'))
            
                        print("Dữ liệu đã được thêm thất bại!")     
                        print('Get data again after:')
                        countdown(600)
                        count +=1
                        if count >= 10 :
                            # 5.5 ghi dữ liệu Extract thất bại vào control_data_file [status= EXTRACT_FAIL]
                            insert_query = "INSERT INTO control_data_file (id_config,name, row_count, status,data_range_from,data_range_to,note,create_at,update_at,create_by,update_by) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                            cursor.execute(insert_query, (1, 'null', 'null', 'EXTRACT_FAIL','null' ,'null', 'crawl', fr'{currentdate}', fr'{currentdate}', 'Nhơn', 'Nhơn'))
                            conn.commit()
                            break
                        else :  continue
                break
            except mysql.connector.Error as err:
                        
                print(f"Lỗi thêm dữ liệu: {err}")
                with open(file_err, 'a') as file:
                 file.write(f'Error: {str(err)}\n')
                count +=1
                # 3.1 kiểm tra lần lặp có lớn hơn 10 không?
                if count >= 10 :break
                countdown(600)
            

                continue  
               
            finally:
                # Đóng cursor và kết nối
                cursor.close()
                conn.close()
         
        else:
            count +=1
            # 3.1 kiểm tra lần lặp có lớn hơn 10 không?
            if count >= 10 :
                err= "connect unsuccess"
                print(f"Lỗi connect db : {err}")
                with open(file_err, 'a') as file:
                 file.write(f'Error: {str(err)}\n')
                break
            print('reconnect last:')
            countdown(600)
            print('start reconnect')
