/*
 Navicat Premium Data Transfer

 Source Server         : serverMart
 Source Server Type    : MySQL
 Source Server Version : 80034 (8.0.34)
 Source Host           : weatherforecastdata.mysql.database.azure.com:3306
 Source Schema         : datamart

 Target Server Type    : MySQL
 Target Server Version : 80034 (8.0.34)
 File Encoding         : 65001

 Date: 20/12/2023 20:34:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for aggregate_weatherdata
-- ----------------------------
DROP TABLE IF EXISTS `aggregate_weatherdata`;
CREATE TABLE `aggregate_weatherdata`  (
  `id_SERIAL` bigint NOT NULL AUTO_INCREMENT,
  `forecastday` datetime NULL DEFAULT NULL,
  `dewPointAvg` float NULL DEFAULT NULL,
  `humidityAvg` float NULL DEFAULT NULL,
  `moonriseTime` datetime NULL DEFAULT NULL,
  `moonsetTime` datetime NULL DEFAULT NULL,
  `precipitationProbabilityMax` float NULL DEFAULT NULL,
  `pressureSurfaceLevelAvg` float NULL DEFAULT NULL,
  `rainAccumulationAvg` float NULL DEFAULT NULL,
  `rainAccumulationLweAvg` float NULL DEFAULT NULL,
  `rainAccumulationLweMax` float NULL DEFAULT NULL,
  `rainAccumulationLweMin` float NULL DEFAULT NULL,
  `rainAccumulationSum` float NULL DEFAULT NULL,
  `sunriseTime` datetime NULL DEFAULT NULL,
  `sunsetTime` datetime NULL DEFAULT NULL,
  `temperatureApparentAvg` float NULL DEFAULT NULL,
  `temperatureApparentMax` float NULL DEFAULT NULL,
  `temperatureApparentMin` float NULL DEFAULT NULL,
  `temperatureAvg` float NULL DEFAULT NULL,
  `temperatureMax` float NULL DEFAULT NULL,
  `temperatureMin` float NULL DEFAULT NULL,
  `uvHealthConcernMax` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `uvIndexMax` float NULL DEFAULT NULL,
  `visibilityAvg` float NULL DEFAULT NULL,
  `weatherCodeMax` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `linkIMG` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `windDirectionAvg` float NULL DEFAULT NULL,
  `windGustAvg` float NULL DEFAULT NULL,
  `windGustMax` float NULL DEFAULT NULL,
  `windSpeedAvg` float NULL DEFAULT NULL,
  `windSpeedMax` float NULL DEFAULT NULL,
  `create_at` datetime NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `expired_at` datetime NULL DEFAULT NULL,
  `create_by` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `update_by` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_SERIAL`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for weatherdata
-- ----------------------------
DROP TABLE IF EXISTS `weatherdata`;
CREATE TABLE `weatherdata`  (
  `id_SERIAL` bigint NOT NULL AUTO_INCREMENT,
  `forecastday` datetime NULL DEFAULT NULL,
  `dewPointAvg` float NULL DEFAULT NULL,
  `humidityAvg` float NULL DEFAULT NULL,
  `moonriseTime` datetime NULL DEFAULT NULL,
  `moonsetTime` datetime NULL DEFAULT NULL,
  `precipitationProbabilityMax` float NULL DEFAULT NULL,
  `pressureSurfaceLevelAvg` float NULL DEFAULT NULL,
  `rainAccumulationAvg` float NULL DEFAULT NULL,
  `rainAccumulationLweAvg` float NULL DEFAULT NULL,
  `rainAccumulationLweMax` float NULL DEFAULT NULL,
  `rainAccumulationLweMin` float NULL DEFAULT NULL,
  `rainAccumulationSum` float NULL DEFAULT NULL,
  `sunriseTime` datetime NULL DEFAULT NULL,
  `sunsetTime` datetime NULL DEFAULT NULL,
  `temperatureApparentAvg` float NULL DEFAULT NULL,
  `temperatureApparentMax` float NULL DEFAULT NULL,
  `temperatureApparentMin` float NULL DEFAULT NULL,
  `temperatureAvg` float NULL DEFAULT NULL,
  `temperatureMax` float NULL DEFAULT NULL,
  `temperatureMin` float NULL DEFAULT NULL,
  `uvHealthConcernMax` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `uvIndexMax` float NULL DEFAULT NULL,
  `visibilityAvg` float NULL DEFAULT NULL,
  `weatherCodeMax` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `linkIMG` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `windDirectionAvg` float NULL DEFAULT NULL,
  `windGustAvg` float NULL DEFAULT NULL,
  `windGustMax` float NULL DEFAULT NULL,
  `windSpeedAvg` float NULL DEFAULT NULL,
  `windSpeedMax` float NULL DEFAULT NULL,
  `create_at` datetime NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `expired_at` datetime NULL DEFAULT NULL,
  `create_by` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `update_by` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_SERIAL`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Procedure structure for copyBeforeCurrentDate
-- ----------------------------
DROP PROCEDURE IF EXISTS `copyBeforeCurrentDate`;
delimiter ;;
CREATE PROCEDURE `copyBeforeCurrentDate`()
BEGIN
    INSERT INTO datamart.aggregate_weatherdata (
        forecastday, dewPointAvg, humidityAvg, moonriseTime, moonsetTime, 
        precipitationProbabilityMax, pressureSurfaceLevelAvg, rainAccumulationAvg, 
        rainAccumulationLweAvg, rainAccumulationLweMax, rainAccumulationLweMin, 
        rainAccumulationSum, sunriseTime, sunsetTime, temperatureApparentAvg, 
        temperatureApparentMax, temperatureApparentMin, temperatureAvg, 
        temperatureMax, temperatureMin, uvHealthConcernMax, uvIndexMax, 
        visibilityAvg, weatherCodeMax, linkIMG, windDirectionAvg, 
        windGustAvg, windGustMax, windSpeedAvg, windSpeedMax, 
        create_at, expired_at, create_by, update_by
    )
    SELECT 
        w.`forecastday`, w.`dewPointAvg`, w.`humidityAvg`, w.`moonriseTime`, 
        w.`moonsetTime`, w.`precipitationProbabilityMax`, w.`pressureSurfaceLevelAvg`, 
        w.`rainAccumulationAvg`, w.`rainAccumulationLweAvg`, w.`rainAccumulationLweMax`, 
        w.`rainAccumulationLweMin`, w.`rainAccumulationSum`, w.`sunriseTime`, 
        w.`sunsetTime`, w.`temperatureApparentAvg`, w.`temperatureApparentMax`, 
        w.`temperatureApparentMin`, w.`temperatureAvg`, w.`temperatureMax`, 
        w.`temperatureMin`, w.`uvHealthConcernMax`, w.`uvIndexMax`, 
        w.`visibilityAvg`, w.`weatherCodeMax`, w.`linkIMG`, w.`windDirectionAvg`, 
        w.`windGustAvg`, w.`windGustMax`, w.`windSpeedAvg`, w.`windSpeedMax`, 
        w.`create_at`, w.`expired_at`, w.`create_by`, w.`update_by`
    FROM datamart.weatherdata w
    WHERE w.`create_at` <= CURRENT_DATE - INTERVAL 1 DAY;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getWeatherData
-- ----------------------------
DROP PROCEDURE IF EXISTS `getWeatherData`;
delimiter ;;
CREATE PROCEDURE `getWeatherData`(IN `date` DATE)
BEGIN
	#Routine body goes here...
SELECT forecastday,temperatureAvg,uvHealthConcernMax,weatherCodeMax,linkIMG,windSpeedAvg,humidityAvg FROM weatherdata WHERE DATE(forecastday) = `date`;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for renameTable
-- ----------------------------
DROP PROCEDURE IF EXISTS `renameTable`;
delimiter ;;
CREATE PROCEDURE `renameTable`()
BEGIN
    RENAME TABLE datamart.aggregate_weatherdata TO temp_table, datamart.weatherdata TO datamart.aggregate_weatherdata ,  temp_table TO datamart.weatherdata;

END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
