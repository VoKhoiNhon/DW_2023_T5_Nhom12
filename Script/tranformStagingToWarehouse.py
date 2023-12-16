import configparser
import json
from datetime import datetime
import mysql.connector
import os
import time
import shutil


def connect(filename):
    db_config = configparser.ConfigParser()
    # 2. đọc file dbControl.ini, dbStaging, dbWarehouse để lấy cấu hình db
    db_config.read(filename)
    host = db_config.get('mysql', 'host')
    user = db_config.get('mysql', 'user')
    password = db_config.get('mysql', 'password')
    database = db_config.get('mysql', 'database')
    try:
        # 3. kết nối db control, staging, warehouse
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        if cnx.is_connected():
            print('Connected to MySQL database: ' + cnx.database)
            return cnx
    except:
        print('connect fail')


def writeDataToDB(data):
    for i in range(len(data)):
        weatherVal = data[i]
        insertData = (
            weatherVal.get('forecastDay'), weatherVal.get('cloudBaseAvg'), weatherVal.get('cloudBaseMax'),
            weatherVal.get('cloudBaseMin'),
            weatherVal.get('cloudCeilingAvg'), weatherVal.get('cloudCeilingMax'), weatherVal.get('cloudCeilingMin'),
            weatherVal.get('cloudCoverAvg'), weatherVal.get('cloudCoverMax'), weatherVal.get('cloudCoverMin'),
            weatherVal.get('dewPointAvg'), weatherVal.get('dewPointMax'), weatherVal.get('dewPointMin'),
            weatherVal.get('evapotranspirationAvg'),
            weatherVal.get('evapotranspirationMax'), weatherVal.get('evapotranspirationMin'),
            weatherVal.get('evapotranspirationSum'),
            weatherVal.get('freezingRainIntensityAvg'), weatherVal.get('freezingRainIntensityMax'),
            weatherVal.get('freezingRainIntensityMin'), weatherVal.get('humidityAvg'),
            weatherVal.get('humidityMax'), weatherVal.get('humidityMin'), weatherVal.get('iceAccumulationAvg'),
            weatherVal.get('iceAccumulationLweAvg'), weatherVal.get('iceAccumulationLweMax'),
            weatherVal.get('iceAccumulationLweMin'),
            weatherVal.get('iceAccumulationLweSum'),
            weatherVal.get('iceAccumulationMax'), weatherVal.get('iceAccumulationMin'),
            weatherVal.get('iceAccumulationSum'),
            weatherVal.get('moonriseTime'), weatherVal.get('moonsetTime'),
            weatherVal.get('precipitationProbabilityAvg'),
            weatherVal.get('precipitationProbabilityMax'),
            weatherVal.get('precipitationProbabilityMin'), weatherVal.get('pressureSurfaceLevelAvg'),
            weatherVal.get('pressureSurfaceLevelMax'), weatherVal.get('pressureSurfaceLevelMin'),
            weatherVal.get('rainAccumulationAvg'),
            weatherVal.get('rainAccumulationLweAvg'),
            weatherVal.get('rainAccumulationLweMax'),
            weatherVal.get('rainAccumulationLweMin'), weatherVal.get('rainAccumulationMax'),
            weatherVal.get('rainAccumulationMin'),
            weatherVal.get('rainAccumulationSum'), weatherVal.get('rainIntensityAvg'),
            weatherVal.get('rainIntensityMax'),
            weatherVal.get('rainIntensityMin'),
            weatherVal.get('sleetAccumulationAvg'), weatherVal.get('sleetAccumulationLweAvg'),
            weatherVal.get('sleetAccumulationLweMax'), weatherVal.get('sleetAccumulationLweMin'),
            weatherVal.get('sleetAccumulationLweSum'), weatherVal.get('sleetAccumulationMax'),
            weatherVal.get('sleetAccumulationMin'),
            weatherVal.get('sleetIntensityAvg'), weatherVal.get('sleetIntensityMax'),
            weatherVal.get('sleetIntensityMin'),
            weatherVal.get('snowAccumulationAvg'), weatherVal.get('snowAccumulationLweAvg'),
            weatherVal.get('snowAccumulationLweMax'),
            weatherVal.get('snowAccumulationLweMin'),
            weatherVal.get('snowAccumulationLweSum'), weatherVal.get('snowAccumulationMax'),
            weatherVal.get('snowAccumulationMin'),
            weatherVal.get('snowAccumulationSum'), weatherVal.get('snowIntensityAvg'),
            weatherVal.get('snowIntensityMax'),
            weatherVal.get('snowIntensityMin'),
            weatherVal.get('sunriseTime'), weatherVal.get('sunsetTime'),
            weatherVal.get('temperatureApparentAvg'),
            weatherVal.get('temperatureApparentMax'), weatherVal.get('temperatureApparentMin'),
            weatherVal.get('temperatureAvg'),
            weatherVal.get('temperatureMax'),
            weatherVal.get('temperatureMin'), weatherVal.get('uvHealthConcernAvg'),
            weatherVal.get('uvHealthConcernMax'),
            weatherVal.get('uvHealthConcernMin'), weatherVal.get('uvIndexAvg'), weatherVal.get('uvIndexMax'),
            weatherVal.get('uvIndexMin'),
            weatherVal.get('visibilityAvg'), weatherVal.get('visibilityMax'), weatherVal.get('visibilityMin'),
            weatherVal.get('weatherCodeMax'), weatherVal.get('weatherCodeMin'), weatherVal.get('windDirectionAvg'),
            weatherVal.get('windGustAvg'),
            weatherVal.get('windGustMax'), weatherVal.get('windGustMin'), weatherVal.get('windSpeedAvg'),
            weatherVal.get('windSpeedMax'),
            weatherVal.get('windSpeedMin'), datetime.now())
        query = "INSERT INTO fact_weather " \
                "(forecastDay,cloudBaseAvg, cloudBaseMax, cloudBaseMin,cloudCeilingAvg,cloudCeilingMax,cloudCeilingMin," \
                "cloudCoverAvg,cloudCoverMax,cloudCoverMin,dewPointAvg,dewPointMax,dewPointMin,evapotranspirationAvg," \
                "evapotranspirationMax,evapotranspirationMin,evapotranspirationSum,freezingRainIntensityAvg," \
                "freezingRainIntensityMax,freezingRainIntensityMin,humidityAvg,humidityMax,humidityMin,iceAccumulationAvg," \
                "iceAccumulationLweAvg,iceAccumulationLweMax,iceAccumulationLweMin,iceAccumulationLweSum,iceAccumulationMax," \
                "iceAccumulationMin,iceAccumulationSum,moonriseTime,moonsetTime,precipitationProbabilityAvg," \
                "precipitationProbabilityMax,precipitationProbabilityMin,pressureSurfaceLevelAvg,pressureSurfaceLevelMax," \
                "pressureSurfaceLevelMin,rainAccumulationAvg,rainAccumulationLweAvg,rainAccumulationLweMax," \
                "rainAccumulationLweMin,rainAccumulationMax,rainAccumulationMin,rainAccumulationSum,rainIntensityAvg," \
                "rainIntensityMax,rainIntensityMin,sleetAccumulationAvg,sleetAccumulationLweAvg,sleetAccumulationLweMax," \
                "sleetAccumulationLweMin,sleetAccumulationLweSum,sleetAccumulationMax,sleetAccumulationMin,sleetIntensityAvg," \
                "sleetIntensityMax,sleetIntensityMin,snowAccumulationAvg,snowAccumulationLweAvg,snowAccumulationLweMax," \
                "snowAccumulationLweMin,snowAccumulationLweSum,snowAccumulationMax,snowAccumulationMin,snowAccumulationSum," \
                "snowIntensityAvg,snowIntensityMax,snowIntensityMin,sunriseTime,sunsetTime,temperatureApparentAvg," \
                "temperatureApparentMax,temperatureApparentMin,temperatureAvg,temperatureMax,temperatureMin,uvHealthConcernAvg," \
                "uvHealthConcernMax,uvHealthConcernMin,uvIndexAvg,uvIndexMax,uvIndexMin,visibilityAvg,visibilityMax,visibilityMin," \
                "weatherCodeMax,weatherCodeMin,windDirectionAvg,windGustAvg,windGustMax,windGustMin,windSpeedAvg,windSpeedMax," \
                "windSpeedMin,create_at) " \
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" \
                ",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursorWarehouse.execute(query, insertData)
    dbWarehouse.commit()


def countdown(t, mess=''):
    print(mess)
    while t:
        minis, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minis, secs)
        print("\r", timer, end="")
        time.sleep(1)
        t -= 1
    print("\r", '00:00', end="")
    print()


def writeLog(idConf=1, status='', note=''):
    cursorControl.callproc('writeLog', args=(idConf, status, note))
    dbControl.commit()
    print(note)


def writeFileLog(status='', note=''):
    # TODO:
    print(note)


def getControlDataFileByDate(status, date):
    cursorControl.callproc('getControlDataFileByDate', args=(status, date))
    resultSet = list(cursorControl.stored_results())
    return resultSet[0].fetchone()


def getDataByDate(date):
    cursorStaging.callproc('getDataByDate', args=(date,))
    resultSet = list(cursorStaging.stored_results())
    return resultSet[0].fetchall()


if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    globalConfig = configparser.ConfigParser()
    isContinue = True

    # 1. đọc file config.ini để lấy cấu hình ban đầu
    globalConfig.read(current_dir + "\config.ini")
    idConfig = int(globalConfig.get('config', 'idConfig'))
    countDownTime = int(globalConfig.get('config', 'countDownTime'))
    loopNum = int(globalConfig.get('config', 'loopNum'))

    loopNumConnectDB = loopNum
    while isContinue:
        fileControl = '\dbconfig\dbControl.ini'
        fileStaging = '\dbconfig\dbStaging.ini'
        fileWarehouse = '\dbconfig\dbWarehouse.ini'

        # 2. đọc file dbControl.ini, dbStaging, dbWarehouse để lấy cấu hình db
        # 3. kết nối db control, staging, warehouse
        dbControl = connect(current_dir + fileControl)
        dbStaging = connect(current_dir + fileStaging)
        dbWarehouse = connect(current_dir + fileWarehouse)

        # 4. kết nối thành công?
        if (dbControl is None) | (dbStaging is None) | (dbWarehouse is None):
            # 4.1 ghi file dữ liệu lỗi vào D:\error_EXTRACT
            writeFileLog('CONNECT_DB_FAIL', 'connect db control, staging, warehouse fail')

            # 4.2 kiểm tra số lần lặp còn lại có <= 0 hay không
            if loopNumConnectDB <= 0:
                isContinue = False

            # 4.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
            loopNumConnectDB -= 1
            countdown(countDownTime, mess='reconnect last:')
            print('start reconnect')
            continue

        cursorControl = dbControl.cursor(dictionary=True)
        cursorStaging = dbStaging.cursor(dictionary=True)
        cursorWarehouse = dbWarehouse.cursor(dictionary=True)
        # 5. Ghi log CONNECT_DB_SUCCESS
        writeLog(idConfig, 'CONNECT_DB_SUCCESS', 'connect db control, staging, warehouse success')

        loopNumGetDataToday = loopNum
        while isContinue:
            # 6. Lấy dữ liệu từ table control_data_file[control] có status = LOAD_FILE_SUCCESS,create_at = [today]
            dataFileToday = getControlDataFileByDate('LOAD_FILE_SUCCESS', datetime.now().date())

            # 7. Kiểm tra có dữ liệu trả về hay không?
            if dataFileToday is None:
                # 7.1 ghi log GET_DATA_FAIL
                writeLog(idConfig, 'GET_DATA_FAIL', 'get data today with status LOAD_SUCCESS not exist')

                # 7.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                if loopNumGetDataToday <= 0:
                    isContinue = False

                # 7.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                loopNumGetDataToday -= 1
                countdown(countDownTime, mess='Get data again after:')
                continue

            # 8. lấy dữ liệu ngày hôm nay từ table weather_data [staging]
            dataToday = getDataByDate(datetime.now().date())

            # 9. Ghi log GET_DATA_SUCCESS
            writeLog(idConfig, 'GET_DATA_SUCCESS', 'get data from staging success')

            # 10. ghi các dữ liệu đã lấy được vào table fact_weather[warehouse]
            writeDataToDB(dataToday)

            # 11. Ghi log INSERT_SUCCESS
            writeLog(idConfig, 'INSERT_SUCCESS', 'insert data to warehouse success')

            # 12. chuyển đổi dữ liệu từ table fact_weather, dim_weather_code, dim_uv_status qua table
            # aggregate_weatherdata
            loopTransformAggregate = loopNum
            while isContinue:
                # 13. Chuyển đổi thành công?
                try:
                    cursorWarehouse.callproc('tranformFactToAggregate', args=(datetime.now().date(),))
                    dbWarehouse.commit()
                except:
                    # 13.1 ghi log TRANSFORM_FAIL
                    writeLog(idConfig, 'TRANSFORM_FAIL', 'transform data to aggregate_weatherdata fail')

                    # 13.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                    if loopTransformAggregate <= 0:
                        isContinue = False

                    # 13.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                    loopTransformAggregate -= 1
                    countdown(countDownTime, mess='Get data again after:')
                    continue

                writeLog(idConfig, 'TRANSFORM_SUCCESS', 'transform data to aggregate_weatherdata success')
                # 15. Thay đổi trạng thái của dữ liệu đã lấy trong table control_data_file status= 'TRANSFORM_SUCCESS'
                cursorControl.callproc("updateStatusDataFile",
                                       args=(dataFileToday['id'], 'TRANSFORM_SUCCESS'))
                dbControl.commit()
                isContinue = False
        # 16. Đóng tất cả kết nối đến các db
        dbStaging.close()
        dbControl.close()
        dbWarehouse.close()
