import configparser
from datetime import datetime
import mysql.connector
import os
import time


def connect(filename):
    # 1 đọc file để lấy cấu hình
    db_config = configparser.ConfigParser()
    db_config.read(filename)
    host = db_config.get('mysql', 'host')
    user = db_config.get('mysql', 'user')
    password = db_config.get('mysql', 'password')
    database = db_config.get('mysql', 'database')
    # 2 connect database
    try:
        cnx = mysql.connector.connect(
            user=user, password=password, host=host, database=database)
        if cnx.is_connected():
            print('Connected to MySQL database')
        return cnx
    except mysql.connector.Error as err:
        print(err)
        with open(file_err, 'a') as file:
            file.write(f'Error: {str(err)}\n')


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
    count = 0
    currentdate = datetime.now().strftime("%Y:%m:%d")
    current_date = datetime.now().strftime("%d%m%Y")
    fileconfigs = '\dbconfig\dbControl.ini'
    configWarehouse = '\dbconfig\dbWarehouse.ini'
    configMart = '\dbconfig\dbMart.ini'
    save_directoryEr = r"D:\error_EXTRACT"
    file_err = fr"{save_directoryEr}\{current_date}_weather_forecast.txt"
    while True:
        # 1 , 2 
        current_dir_CT = os.path.dirname(__file__) + fileconfigs
        connctrl = connect(current_dir_CT)
        current_dir_WH = os.path.dirname(__file__) + configWarehouse
        connWh = connect(current_dir_WH)
        current_dir_M = os.path.dirname(__file__) + configMart
        connM = connect(current_dir_M)
        # 3 kiểm tra kết nối đến cơ sở dữ liệu
        if connctrl is not None and connWh is not None and connM is not None:
            try:
                controlcursor = connctrl.cursor()
                # 4 ghi log thành công
                insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                controlcursor.execute(insert_query, (
                    1, 'CONNECT_DB_SUCCESS', 'lconnect CONTROL, WAREHOUSE, MART success', fr'{currentdate}'))
                connctrl.commit()
                # 5. Lấy dữ liệu từ dbControl với STATUS= TRANSFORM_SUCCESS và create_at= CURRENT_DATE
                controlcursor.callproc('getDataFileToday', ('TRANSFORM_SUCCESS',))
                status = list(controlcursor.stored_results())
                st = status[0].fetchone()
                print(st)
                while (True):
                    # 6. kiểm tra dữ liệu vừa lấy có tồn tại không
                    if st is not None:
                        martcursor = connM.cursor()
                        # 7. truncat bảng aggregate_weatherdata ở datamart
                        use_query = f"USE datamart"
                        martcursor.execute(use_query)
                        truncate_query = f"TRUNCATE TABLE aggregate_weatherdata "
                        martcursor.execute(truncate_query)

                        print('truncat success')

                        # 8. copy dữ liệu trước ngày hôm nay từ bảng weatherdata sang bảng aggregate_weatherdata ở datamart
                        martcursor.callproc('copyBeforeCurrentDate')

                        print('copy data success')
                        # 9. lấy dữ liệu cần insert ngày hôm nay aggregate_weatherdata ở warehouse
                        whcursor = connWh.cursor()
                        source_cursor = whcursor.callproc('getDataAggerateCurrentDate')
                        sourcewh = list(whcursor.stored_results())

                        rows = sourcewh[0].fetchall()
                        # 10 ghi dữ liệu vào bảng aggregate_weatherdata ở datamart
                        for row in rows:
                            insertQ = 'INSERT INTO `datamart`.`aggregate_weatherdata` ( `forecastday`, `dewPointAvg`, ' \
                                      '`humidityAvg`, `moonriseTime`, `moonsetTime`, `precipitationProbabilityMax`,' \
                                      ' `pressureSurfaceLevelAvg`, `rainAccumulationAvg`, `rainAccumulationLweAvg`,' \
                                      ' `rainAccumulationLweMax`, `rainAccumulationLweMin`, `rainAccumulationSum`, ' \
                                      '`sunriseTime`, `sunsetTime`, `temperatureApparentAvg`, `temperatureApparentMax`, ' \
                                      '`temperatureApparentMin`, `temperatureAvg`, `temperatureMax`, `temperatureMin`, ' \
                                      '`uvHealthConcernMax`, `uvIndexMax`, `visibilityAvg`, `weatherCodeMax`,`linkIMG`,' \
                                      ' `windDirectionAvg`, `windGustAvg`, `windGustMax`, `windSpeedAvg`, `windSpeedMax`,' \
                                      ' `create_at`, `expired_at`, `create_by`, `update_by`) ' \
                                      'VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s,' \
                                      ' %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s);'
                            martcursor.execute(insertQ, (
                                row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                row[11],
                                row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20],
                                row[21],
                                row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30],
                                row[31],
                                row[32], row[33], row[34]))

                        print('insert success')
                        # 11. đổi tên bảng aggregate_weatherdata và weatherdata ở datamart
                        martcursor.callproc('renameTable')
                        connM.commit()
                        print('rename success')

                        # 12. ghi log load mart thành công
                        insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                        controlcursor.execute(insert_query,
                                              (1, 'LOAD_MART_SUCCESS', 'load mart success', fr'{currentdate}'))

                        # 13. update dữ liệu LOAD_MART_SUCCESS thành công vào control_data_file [status= LOAD_MART_SUCCESS]
                        insert_query = "UPDATE control_data_file SET  status= %s WHERE Date(control_data_file.update_at)= CURRENT_DATE"
                        controlcursor.execute(insert_query, ('LOAD_MART_SUCCESS',))
                        connM.commit()
                        connWh.commit()
                        connctrl.commit()
                        # 14. đóng connection tất cả database
                        martcursor.close()
                        whcursor.close()
                        connWh.close()
                        connM.close()
                        print("Dữ liệu đã được thêm thành công!")
                        break
                    else:
                        # 15. ghi log load mart thất bại
                        insert_query = "INSERT INTO log (id_config, status,note,log_date) VALUES (%s, %s, %s,%s)"
                        controlcursor.execute(insert_query,
                                              (1, 'LOAD_MART_UNSUCCESS', 'load mart unsuccess', fr'{currentdate}'))
                        connctrl.commit()
                        print('Get data again after:')
                        countdown(600)
                        count += 1
                        if count >= 10:
                            # 16. update dữ liệu LOAD MART thất bại vào control_data_file [status= LOAD_MART_UNSUCCESS]
                            insert_query = "UPDATE control_data_file SET  status= %s WHERE Date(control_data_file.update_at)= CURRENT_DATE"
                            controlcursor.execute(insert_query, ('LOAD_MART_UNSUCCESS',))
                            connctrl.commit()
                            break
                        else:
                            continue

            except mysql.connector.Error as err:
                print(f"Lỗi thêm dữ liệu: {err}")
                # ghi dữ liệu lỗi
                with open(file_err, 'a') as file:
                    file.write(f'Error: {str(err)}\n')
                count += 1
                # 3.1 kiểm tra lần lặp có lớn hơn 10 không?
                if count >= 10: break
                countdown(600)
                continue
            finally:
                # 17 đóng kết nối db control
                controlcursor.close()
                connctrl.close()
            break
        else:
            # 3.1 kiểm tra lần lặp có lớn hơn 10 không?
            count += 1
            if count >= 10:
                err = "connect unsuccess"
                print(f"Lỗi connect db : {err}")
                with open(file_err, 'a') as file:
                    file.write(f'Error: {str(err)}\n')
                break
            print('reconnect last:')
            countdown(600)
            print('start reconnect')
