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
    currentdate = datetime.now().strftime("%Y:%m:%d")
    current_date = datetime.now().strftime("%d%m%Y")
    fileconfigs='\dbconfig\dbControl.ini'
    configWarehouse='\dbconfig\dbWarehouse.ini'
    configMart='\dbconfig\dbMart.ini'
    while True :
        current_dir_CT = os.path.dirname(__file__)+fileconfigs
        connctrl= connect( current_dir_CT)
        current_dir_WH = os.path.dirname(__file__)+configWarehouse
        connWh= connect( current_dir_WH)
        current_dir_M = os.path.dirname(__file__)+configMart
        connM= connect( current_dir_M)
        if connctrl is not None and connWh is not None and connM is not None :
            try:
                controlcursor = connctrl.cursor()
                controlcursor.callproc('getDataFileToday',('EXTRACT_SUCCESS',))
                status=list(controlcursor.stored_results())
                st=status[0].fetchone()
                print(st)
                if  st is not None:
                    martcursor=connM.cursor()
                    use_query = f"USE datamart"
                    martcursor.execute(use_query)
                    truncate_query = f"TRUNCATE TABLE aggregate_weatherdata "
                    martcursor.execute(truncate_query)
                    print('truncat success')
                   
                    martcursor.callproc('copyBeforeCurrentDate')

                    whcursor = connWh.cursor()
                    source_cursor=whcursor.callproc('getDataAggerateCurrentDate')
                    sourcewh= list(whcursor.stored_results())
                  
                    # for re in sourcewh:
                    rows = sourcewh[0].fetchall()
                    for row in rows:                       
                        insertQ ='INSERT INTO `datamart`.`aggregate_weatherdata` ( `forecastday`, `dewPointAvg`, `humidityAvg`, `moonriseTime`, `moonsetTime`, `precipitationProbabilityMax`, `pressureSurfaceLevelAvg`, `rainAccumulationAvg`, `rainAccumulationLweAvg`, `rainAccumulationLweMax`, `rainAccumulationLweMin`, `rainAccumulationSum`, `sunriseTime`, `sunsetTime`, `temperatureApparentAvg`, `temperatureApparentMax`, `temperatureApparentMin`, `temperatureAvg`, `temperatureMax`, `temperatureMin`, `uvHealthConcernMax`, `uvIndexMax`, `visibilityAvg`, `weatherCodeMax`,`linkIMG`, `windDirectionAvg`, `windGustAvg`, `windGustMax`, `windSpeedAvg`, `windSpeedMax`, `create_at`, `expired_at`, `create_by`, `update_by`) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s);'
                        martcursor.execute(insertQ,(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34]))

                    print('insert success')

                    martcursor.callproc('renameTable')     
                    print('rename success')                

                    # 5.2 ghi log thành công
                    insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                    controlcursor.execute(insert_query, (1, 'LOAD_MART_SUCCESS', 'load mart success', fr'{currentdate}'))
                   
                    # # 5.3 ghi dữ liệu Extract thành công vào control_data_file [status= LOAD_MART_SUCCESS]
                    insert_query = "UPDATE control_data_file SET  status= %s WHERE Date(control_data_file.update_at)= CURRENT_DATE"
                    controlcursor.execute(insert_query, ('LOAD_MART_SUCCESS',))
                    connM.commit()
                    connWh.commit()
                    connctrl.commit()

                    martcursor.close()
                    whcursor.close()
                    connWh.close()
                    connM.close()
                    print("Dữ liệu đã được thêm thành công!")
            except mysql.connector.Error as err:
                insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                controlcursor.execute(insert_query, (1, 'LOAD_MART_UNSUCCESS', 'load mart unsuccess', fr'{currentdate}'))
                connctrl.commit()
          
                print(f"Lỗi thêm dữ liệu: {err}")
            finally:
             
                controlcursor.close()
                connctrl.close()
            break 
        else:  time.sleep(60)
 



