import configparser
import requests
import json
from datetime import datetime
import mysql.connector
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
def getDataFromAPI() :
    if response.status_code == 200:
        current_date = datetime.now().strftime("%d%m%Y")
        save_directory = r"D:\weather_data_Staging"
        file_name = fr"{save_directory}\{current_date}_weather_forecast.json"
        with open(file_name, "w") as json_file:
            json.dump(response.json(), json_file, indent=4)
        print(f"Dữ liệu đã được lưu vào {file_name}")
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
def WriteDatatoDB(data, filename):
    conn= connect(filename)
    if conn is not None:
        try:
            if response.status_code==200:
                cursor = conn.cursor()
                insert_query = "INSERT INTO control_data_file_configs (column1, column2, column3) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (data['value1'], data['value2'], data['value3']))
                conn.commit()
                print("Dữ liệu đã được thêm thành công!")
        except mysql.connector.Error as err:
            print(f"Lỗi thêm dữ liệu: {err}")
        finally:
             # Đóng cursor và kết nối
            cursor.close()
            conn.close()
if __name__ == '__main__':
    # filename= 'D:\Warehouse\DW_2023_T5_Nhom12\Script\dbControl.ini'
    # connect(filename)
    getDataFromAPI()
 



