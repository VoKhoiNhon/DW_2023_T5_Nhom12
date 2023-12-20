/*
 Navicat Premium Data Transfer

 Source Server         : aaaaa
 Source Server Type    : MySQL
 Source Server Version : 100432 (10.4.32-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : staging

 Target Server Type    : MySQL
 Target Server Version : 100432 (10.4.32-MariaDB)
 File Encoding         : 65001

 Date: 20/12/2023 20:33:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for load_weather_data
-- ----------------------------
DROP TABLE IF EXISTS `load_weather_data`;
CREATE TABLE `load_weather_data`  (
  `forecastDay` datetime NULL DEFAULT NULL,
  `cloudBaseAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudBaseMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudBaseMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCeilingAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCeilingMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCeilingMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCoverAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCoverMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCoverMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `dewPointAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `dewPointMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `dewPointMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `freezingRainIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `freezingRainIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `freezingRainIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `humidityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `humidityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `humidityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `moonriseTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `moonsetTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `precipitationProbabilityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `precipitationProbabilityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `precipitationProbabilityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pressureSurfaceLevelAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pressureSurfaceLevelMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pressureSurfaceLevelMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sunriseTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sunsetTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureApparentAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureApparentMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureApparentMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvHealthConcernAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvHealthConcernMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvHealthConcernMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvIndexAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvIndexMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvIndexMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `visibilityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `visibilityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `visibilityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `weatherCodeMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `weatherCodeMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windDirectionAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windGustAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windGustMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windGustMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windSpeedAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windSpeedMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windSpeedMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `create_at` datetime NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for weather_data
-- ----------------------------
DROP TABLE IF EXISTS `weather_data`;
CREATE TABLE `weather_data`  (
  `id_SERIAL` bigint NOT NULL AUTO_INCREMENT,
  `forecastDay` datetime NULL DEFAULT NULL,
  `cloudBaseAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudBaseMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudBaseMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCeilingAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCeilingMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCeilingMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCoverAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCoverMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `cloudCoverMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `dewPointAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `dewPointMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `dewPointMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `evapotranspirationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `freezingRainIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `freezingRainIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `freezingRainIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `humidityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `humidityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `humidityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationLweSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `iceAccumulationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `moonriseTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `moonsetTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `precipitationProbabilityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `precipitationProbabilityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `precipitationProbabilityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pressureSurfaceLevelAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pressureSurfaceLevelMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pressureSurfaceLevelMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainAccumulationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `rainIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationLweSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sleetIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationLweSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowAccumulationSum` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowIntensityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowIntensityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `snowIntensityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sunriseTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `sunsetTime` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureApparentAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureApparentMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureApparentMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `temperatureMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvHealthConcernAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvHealthConcernMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvHealthConcernMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvIndexAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvIndexMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `uvIndexMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `visibilityAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `visibilityMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `visibilityMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `weatherCodeMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `weatherCodeMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windDirectionAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windGustAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windGustMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windGustMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windSpeedAvg` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windSpeedMax` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `windSpeedMin` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `create_at` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id_SERIAL`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Procedure structure for getDataByDate
-- ----------------------------
DROP PROCEDURE IF EXISTS `getDataByDate`;
delimiter ;;
CREATE PROCEDURE `getDataByDate`(IN date DATE)
BEGIN
    #Routine body goes here...
SELECT * FROM weather_data WHERE DATE(create_at) = date;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for transformData
-- ----------------------------
DROP PROCEDURE IF EXISTS `transformData`;
delimiter ;;
CREATE PROCEDURE `transformData`(IN p_date DATE)
BEGIN
    #Routine body goes here...
         INSERT INTO weather_data
     SELECT NULL, l.* FROM load_weather_data l WHERE DATE(create_at) = p_date ;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
