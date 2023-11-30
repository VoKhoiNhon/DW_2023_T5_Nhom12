import configparser
from datetime import datetime
import mysql.connector
import os
import time



def connect(filename):
    db_config = configparser.ConfigParser()
    db_config.read(filename)
    host = db_config.get('mysql', 'host')
    user = db_config.get('mysql', 'user')
    password = db_config.get('mysql', 'password')
    database = db_config.get('mysql', 'database')
    try:
        cnx = mysql.connector.connect(
            user=user, password=password, host=host, database=database)
        if cnx.is_connected():
            print('Connected to MySQL database')
        return cnx
    except mysql.connector.Error as err:
        print(err)

        
if __name__ == '__main__':
    current_date = datetime.now().strftime("%d%m%Y")
    fileconfigs='\dbconfig\dbControl.ini'
    configWarehouse='\dbconfig\dbWarehouse.ini'
    configMart='\dbconfig\dbMart.ini'
    while True :
        current_dir_CT = os.path.dirname(__file__)+fileconfigs
        connctrl= connect( current_dir_CT)
        print(current_dir_CT)
        current_dir_WH = os.path.dirname(__file__)+configWarehouse
        connWh= connect( current_dir_WH)
        current_dir_M = os.path.dirname(__file__)+configMart
        connM= connect( current_dir_M)
        if connctrl is not None and connWh is not None  :
            try:
                controlcursor = connctrl.cursor()
                controlcursor.execute("SELECT status FROM control_data_file WHERE id = (SELECT MAX(id) FROM control_data_file)")
                status=controlcursor.fetchone()
                print(status[0])
                if  status[0] == 'TRANSFORM SUCCESS':
                 
                    whcursor = connWh.cursor()
                    source_cursor=whcursor.execute("select * from datamart.aggregate_weatherdata order by create_at DESC limit 6")
                    data_to_transfer = whcursor.fetchall()
                    # insert_query = "INSERT INTO control_data_file (id_config,name, row_count, status,data_range_from,data_range_to,note,create_at,update_at,create_by,update_by) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                    # cursor.execute(insert_query, ( 1, '{current_date}_weather_forecast.json',6,'EXTRACT SUCCESS',dataforecast['timelines']['daily'][0]['time'],dataforecast['timelines']['daily'][5]['time'],'crawl', datetime.now().strftime("%d:%m:%Y"),datetime.now().strftime("%d:%m:%Y"),'Nhơn','Nhơn'))
                    # insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                    # cursor.execute(insert_query, ( 1, 'EXTRACT SUCCESS','crawl success', datetime.now().strftime("%d:%m:%Y")))
                    connctrl.commit()
                    # print("Dữ liệu đã được thêm thành công!")
            except mysql.connector.Error as err:
                # insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                # cursor.execute(insert_query, ( 1, 'LOAD MART FAIL','load unsuccess', datetime.now().strftime("%d:%m:%Y")))
                # connctrl.commit()
          
                print(f"Lỗi thêm dữ liệu: {err}")
            finally:
                # Đóng cursor và kết nối
            
               
                
                connWh.close()
          
                controlcursor.close()
                # whcursor.close()
                connctrl.close()
            break 
        else:  time.sleep(60)
 



