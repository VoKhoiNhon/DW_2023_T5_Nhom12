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


def convertTime(time):
    return datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")


def writeFileToDB(data):
    listWeatherDay = data['timelines']['daily']
    for i in range(len(listWeatherDay)):
        foresCast = convertTime(listWeatherDay[i]['time'])
        weatherVal = listWeatherDay[i]['values']

        insertData = (
            foresCast, weatherVal.get('cloudBaseAvg'), weatherVal.get('cloudBaseMax'), weatherVal.get('cloudBaseMin'),
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
            convertTime(weatherVal.get('moonriseTime')), convertTime(weatherVal.get('moonsetTime')),
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
            convertTime(weatherVal.get('sunriseTime')), convertTime(weatherVal.get('sunsetTime')),
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
        query = "INSERT INTO load_weather_data " \
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
        cursorStaging.execute(query, insertData)
    dbStaging.commit()


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


def getConfig(ConfigId):
    cursorControl.callproc('getConfig', args=(ConfigId,))
    resultSet = list(cursorControl.stored_results())
    return resultSet[0].fetchone()


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
        # 2. đọc file dbControl.ini, dbStaging, dbWarehouse để lấy cấu hình db
        # 3. kết nối db control, staging, warehouse
        dbControl = connect(current_dir + fileControl)
        dbStaging = connect(current_dir + fileStaging)

        # 4. kết nối thành công?
        if (dbControl is None) | (dbStaging is None):
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

        # 5. Ghi log CONNECT_DB_SUCCESS
        writeLog(idConfig, 'CONNECT_DB_SUCCESS', 'connect db control and staging success')

        loopNumGetConfig = loopNum
        while isContinue:
            # 6. lấy config trong table control_data_file_config dựa trên field idConfig[config.ini]
            config = getConfig(idConfig)

            # 7.có dữ liệu trả về?
            if config is None:
                # 7.1 ghi log GET_CONFIG_FAIL
                writeFileLog('GET_CONFIG_FAIL', 'get config fail')

                # 7.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                if loopNumGetConfig <= 0:
                    isContinue = False

                # 7.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                loopNumGetConfig -= 1
                countdown(countDownTime, mess='reconnect last:')
                print('start reconnect')
                continue

            # 8. ghi log GET_CONFIG_SUCCESS
            writeFileLog('GET_CONFIG_SUCCESS', 'get config success')

            loopNumGetControlFile = loopNum
            while isContinue:
                # 9. Lấy dữ liệu từ table control_data_file[control] có status = EXTRACT_SUCCESS,create_at = [today]
                dataFileToday = getControlDataFileByDate('EXTRACT_SUCCESS', datetime.now().date())

                # 10.có dữ liệu trả về?
                if dataFileToday is None:
                    # 10.1 ghi log GET_CONFIG_FILE_FAIL
                    writeFileLog('GET_CONFIG_FILE_FAIL', 'get config file fail')

                    # 10.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                    if loopNumGetControlFile <= 0:
                        isContinue = False

                    # 10.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                    loopNumGetControlFile -= 1
                    countdown(countDownTime, mess='reconnect last:')
                    print('start reconnect')
                    continue

                # 11. đọc file json đã được tải về thông qua trường location[config] + name[control_data_file]
                locationFile = config['location'] + '\\' + dataFileToday['name']
                loopNumReadFile = loopNum
                while isContinue:
                    # 12. Đọc thành công?
                    try:
                        with open(locationFile, 'r') as file:
                            jsonData = json.load(file)
                    except:
                        # 12.1 ghi log READ_FILE_FAIL
                        writeFileLog('READ_FILE_FAIL', 'read file fail')

                        # 12.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                        if loopNumReadFile <= 0:
                            isContinue = False

                        # 12.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                        loopNumReadFile -= 1
                        countdown(countDownTime, mess='reconnect last:')
                        print('start reconnect')
                        continue

                    # 13. ghi log READ_FILE_SUCCESS
                    writeFileLog('READ_FILE_SUCCESS', 'read file success')

                    # 14. backup file qua folder theo destination[control_data_file_config]
                    try:
                        shutil.copy(locationFile, config['destination'])
                        writeLog(idConfig, 'BACKUP_SUCCESS',
                                 'backup file ' + dataFileToday['name'] + ' to ' + config['destination'] + ' success')
                    except:
                        # 15.1 ghi log BACKUP_FILE_FAIL
                        writeFileLog('BACKUP_FILE_FAIL', 'backup file fail')

                        # 12.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                        if loopNumReadFile <= 0:
                            isContinue = False

                        # 12.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                        loopNumReadFile -= 1
                        countdown(countDownTime, mess='reconnect last:')
                        print('start reconnect')
                        continue

                    # 16. ghi log BACKUP_FILE_SUCCESS
                    writeFileLog('BACKUP_FILE_SUCCESS', 'backup file success')

                    loopNumWriteToDB = loopNum
                    # 17. ghi dữ liệu lấy từ file vào  table load_weather_data[staging]
                    while isContinue:
                        # 18. ghi thành công?
                        try:
                            writeFileToDB(jsonData)
                        except mysql.connector.Error as err:
                            # 18.1 ghi log WRITE_TO_DB_FAIL
                            writeFileLog('WRITE_TO_DB_FAIL', 'write file to db fail')

                            # 18.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                            if loopNumWriteToDB <= 0:
                                isContinue = False

                            # 18.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                            loopNumWriteToDB -= 1
                            countdown(countDownTime, mess='reconnect last:')
                            print('start reconnect')
                            continue

                        # 19. ghi log WRITE_TO_DB_SUCCESS
                        writeLog(idConfig, 'WRITE_TO_DB_SUCCESS', 'load file to staging success')

                        # 20. Chuyển đổi dữ liệu từ table load_weather_data qua table weather_data
                        # 21. ghi thành công?
                        try:
                            cursorStaging.callproc('transformData', args=(datetime.now().date(),))
                            dbStaging.commit()
                        except:
                            # 21.1 ghi log TRANSFORM_DATA_FAIL
                            writeFileLog('TRANSFORM_DATA_FAIL',
                                         'transform table load_weather_data to table weather_data fail')

                            # 18.2 kiểm tra số lần lặp còn lại có <= 0 hay không
                            if loopNumWriteToDB <= 0:
                                isContinue = False

                            # 18.3 giảm số lần lặp còn lại đi 1 và đợi 10 phút
                            loopNumWriteToDB -= 1
                            countdown(countDownTime, mess='reconnect last:')
                            print('start reconnect')
                            continue

                        # 22. ghi log TRANSFORM_DATA_SUCCESS
                        writeLog(idConfig, 'TRANSFORM_DATA_SUCCESS',
                                 'transform table load_weather_data to table weather_data success')

                        # 23. ghi log LOAD_FILE_SUCCESS
                        writeLog(idConfig, 'LOAD_FILE_SUCCESS', 'load file success')

                        # 24. thay đổi trạng thái file hiện tại trong table control_data_file thành LOAD_FILE_SUCCESS
                        cursorControl.callproc("updateStatusDataFile",
                                               args=(dataFileToday['id'], 'LOAD_FILE_SUCCESS'))
                        dbControl.commit()
                        isContinue = False
        # 25. Đóng tất cả kết nối đến các db
        dbStaging.close()
        dbControl.close()
