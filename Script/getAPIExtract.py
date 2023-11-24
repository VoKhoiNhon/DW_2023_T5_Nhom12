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
response = requests.get(api_url, params=params)

def connect(filename):
    db_config = configparser.ConfigParser()
    db_config.read(filename)
    host = db_config.get('mysql','host')
    user = db_config.get('mysql','user')
    password = db_config.get('mysql','password')
    database = db_config.get('mysql','database')
    cnx = mysql.connector.connect(user=user, password=password,host=host,database=database)
    if cnx.is_connected():
        print('Connected to MySQL database')
        return cnx

    
def getDataFromAPI() :
    if response.status_code == 200:
        current_date = datetime.now().strftime("%d%m%Y")
        save_directory = r"D:\weather_data_Staging"
        file_name = fr"{save_directory}\{current_date}_weather_forecast.json"
        with open(file_name, "w") as json_file:
            json.dump(response.json(), json_file, indent=4)
        print(f"Dữ liệu đã được lưu vào {file_name}")
        return True
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
        return False
    
if __name__ == '__main__':
    current_date = datetime.now().strftime("%d%m%Y")
    save_directory = r"D:\weather_data_Staging"
    file_name = fr"{save_directory}\{current_date}_weather_forecast.json"
    fileconfigs='\dbconfig\dbControl.ini'
    current_dir = os.path.dirname(__file__)+fileconfigs
    print(current_dir)
    print (connect( current_dir))
    conn= connect( current_dir)
    print(conn)
    while True :
        if conn is not None :
            try:
                cursor = conn.cursor()
                if  response.status_code == 200:
                    with open(file_name, 'r') as file:
                                        dataforecast = json.load(file)
                    insert_query = "INSERT INTO control_data_file (id_config,name, row_count, status,data_range_from,data_range_to,note,create_at,update_at,create_by,update_by) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                    cursor.execute(insert_query, ( 1, '{current_date}_weather_forecast.json',6,'EXTRACT SUCCESS',dataforecast['timelines']['daily'][0]['time'],dataforecast['timelines']['daily'][5]['time'],'crawl', datetime.now().strftime("%d:%m:%Y"),datetime.now().strftime("%d:%m:%Y"),'Nhơn','Nhơn'))
                    insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                    cursor.execute(insert_query, ( 1, 'EXTRACT SUCCESS','crawl success', datetime.now().strftime("%d:%m:%Y")))
                    conn.commit()
                    print("Dữ liệu đã được thêm thành công!")
            except mysql.connector.Error as err:
                insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                cursor.execute(insert_query, ( 1, 'EXTRACT FAIL','crawl unsuccess', datetime.now().strftime("%d:%m:%Y")))
                conn.commit()
                print(f"Lỗi thêm dữ liệu: {err}")
            finally:
                # Đóng cursor và kết nối
                cursor.close()
                conn.close()
            break 
        else:  time.sleep(60)
 



