import configparser
import requests
import json
from datetime import datetime
import mysql.connector
import os
import time
import shutil


def connect(filename):
    db_config = configparser.ConfigParser()
    db_config.read(filename)
    host = db_config.get('mysql', 'host')
    user = db_config.get('mysql', 'user')
    password = db_config.get('mysql', 'password')
    database = db_config.get('mysql', 'database')
    try:
        cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
        if cnx.is_connected():
            print('Connected to MySQL database: ' + cnx.database)
            return cnx
    except:
        print('connect fail')


def countdown(t):
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


def writeLog(status='', note=''):
    query = "INSERT INTO log (status, note, log_date) VALUES ( %s, %s,%s)"
    insertData = (status, note, datetime.now())
    cursorControl.execute(query, insertData)
    dbControl.commit()
    print(note)


if __name__ == '__main__':
    fileControl = '\dbconfig\dbControl.ini'
    fileStaging = '\dbconfig\dbStaging.ini'
    current_dir = os.path.dirname(__file__)

    while True:
        # 1. Kết nối DB control và DB staging
        dbControl = connect(current_dir + fileControl)
        dbStaging = connect(current_dir + fileStaging)
        # 2. Kết nối thành công?
        if (dbControl is not None) & (dbStaging is not None):
            cursorControl = dbControl.cursor(dictionary=True)
            cursorStaging = dbStaging.cursor(dictionary=True)

            # 3.1. Ghi log kết nối thành công
            writeLog('CONNECT_DB_SUCCESS', 'connect db control and staging success')

            # 4. Lấy trường dữ liệu is_delete = 0 trong table control_data_file_config
            cursorControl.execute('SELECT * FROM control_data_file_configs WHERE is_delete = 0')
            result = cursorControl.fetchall()
            config = result[0]

            while True:
                # 5. Lấy trường dữ liệu ngày hôm nay từ table control_data_file
                currentDate = datetime.now()
                cursorControl.execute(
                    'SELECT * FROM control_data_file WHERE DATE(create_at) = %s', (currentDate.date(),))
                result = cursorControl.fetchall()
                dataFileToday = result[0]

                # 6. status = EXTRACT_SUCCESS?
                if dataFileToday['status'] == 'EXTRACT_SUCCESS':
                    # 7.1. Đọc file theo đường dẫn từ trường location của table config và name của table control_data_file
                    locationFile = config['location'] + '\\' + dataFileToday['name']

                    # 8. File tồn tại?
                    try:
                        with open(locationFile, 'r') as file:
                            jsonData = json.load(file)
                    except:
                        # 7.2 Đợi 10 phút
                        print('Get data again after:')
                        countdown(600)
                        continue

                    # 9. Backup file vào folder theo trường destination trong table config
                    # 10. Backup thành công?
                    try:
                        shutil.copy(locationFile, config['destination'])
                        # 11. Ghi log backup thành công
                        writeLog('BACKUP_SUCCESS',
                                 'backup file ' + dataFileToday['name'] + ' to ' + config['destination'] + ' success')
                    except:
                        # 7.2 Đợi 10 phút
                        print('Get data again after:')
                        countdown(600)
                        continue

                    # 12. Ghi dữ liệu từ file đã đọc vào bảng load_weather_data
                    # 13. Ghi thành công?
                    try:
                        writeFileToDB(jsonData)
                        # 14. Ghi log load file thành công và control_data_file status = "LOAD_FILE_SUCCESS"
                        writeLog('LOAD_FILE_SUCCESS', 'load file to staging success')
                        cursorControl.execute("UPDATE control_data_file SET status = %s WHERE id = %s",
                                              ('LOAD_FILE_SUCCESS', dataFileToday['id']))
                        dbControl.commit()

                    except mysql.connector.Error as err:
                        # 14.2 Ghi log load file không thành công
                        writeLog('LOAD_FILE_FAIL', 'load file to staging not success')
                        print(f"load file error: {err}")
                        # 7.2 Đợi 10 phút
                        print('Get data again after:')
                        countdown(600)
                        continue

                    break
                else:
                    # 7.2 Đợi 10 phút
                    print('Get data again after:')
                    countdown(600)
            break
        # 3.2. Đợi 10 phút
        else:
            # TODO  writeLog('not done')
            print('reconnect last:')
            countdown(600)
            print('start reconnect')
