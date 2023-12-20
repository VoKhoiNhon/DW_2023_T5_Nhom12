/*
 Navicat Premium Data Transfer

 Source Server         : aaaaa
 Source Server Type    : MySQL
 Source Server Version : 100432 (10.4.32-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : warehouse

 Target Server Type    : MySQL
 Target Server Version : 100432 (10.4.32-MariaDB)
 File Encoding         : 65001

 Date: 20/12/2023 20:33:57
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
  `uvHealthConcernMax` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `uvIndexMax` float NULL DEFAULT NULL,
  `visibilityAvg` float NULL DEFAULT NULL,
  `weatherCodeMax` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `linkIMG` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `windDirectionAvg` float NULL DEFAULT NULL,
  `windGustAvg` float NULL DEFAULT NULL,
  `windGustMax` float NULL DEFAULT NULL,
  `windSpeedAvg` float NULL DEFAULT NULL,
  `windSpeedMax` float NULL DEFAULT NULL,
  `create_at` datetime NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `expired_at` datetime NULL DEFAULT NULL,
  `create_by` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_by` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_SERIAL`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for dim_uv_status
-- ----------------------------
DROP TABLE IF EXISTS `dim_uv_status`;
CREATE TABLE `dim_uv_status`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` int NOT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `expried` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `code`) USING BTREE,
  INDEX `code`(`code` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_vietnamese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for dim_weather_code
-- ----------------------------
DROP TABLE IF EXISTS `dim_weather_code`;
CREATE TABLE `dim_weather_code`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` int NOT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `link_icon` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `expried` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `code`) USING BTREE,
  INDEX `code`(`code` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_vietnamese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for fact_weather
-- ----------------------------
DROP TABLE IF EXISTS `fact_weather`;
CREATE TABLE `fact_weather`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `forecastDay` datetime NULL DEFAULT NULL,
  `cloudBaseAvg` float NULL DEFAULT NULL,
  `cloudBaseMax` float NULL DEFAULT NULL,
  `cloudBaseMin` float NULL DEFAULT NULL,
  `cloudCeilingAvg` float NULL DEFAULT NULL,
  `cloudCeilingMax` float NULL DEFAULT NULL,
  `cloudCeilingMin` float NULL DEFAULT NULL,
  `cloudCoverAvg` float NULL DEFAULT NULL,
  `cloudCoverMax` float NULL DEFAULT NULL,
  `cloudCoverMin` float NULL DEFAULT NULL,
  `dewPointAvg` float NULL DEFAULT NULL,
  `dewPointMax` float NULL DEFAULT NULL,
  `dewPointMin` float NULL DEFAULT NULL,
  `evapotranspirationAvg` float NULL DEFAULT NULL,
  `evapotranspirationMax` float NULL DEFAULT NULL,
  `evapotranspirationMin` float NULL DEFAULT NULL,
  `evapotranspirationSum` float NULL DEFAULT NULL,
  `freezingRainIntensityAvg` float NULL DEFAULT NULL,
  `freezingRainIntensityMax` float NULL DEFAULT NULL,
  `freezingRainIntensityMin` float NULL DEFAULT NULL,
  `humidityAvg` float NULL DEFAULT NULL,
  `humidityMax` float NULL DEFAULT NULL,
  `humidityMin` float NULL DEFAULT NULL,
  `iceAccumulationAvg` float NULL DEFAULT NULL,
  `iceAccumulationLweAvg` float NULL DEFAULT NULL,
  `iceAccumulationLweMax` float NULL DEFAULT NULL,
  `iceAccumulationLweMin` float NULL DEFAULT NULL,
  `iceAccumulationLweSum` float NULL DEFAULT NULL,
  `iceAccumulationMax` float NULL DEFAULT NULL,
  `iceAccumulationMin` float NULL DEFAULT NULL,
  `iceAccumulationSum` float NULL DEFAULT NULL,
  `moonriseTime` datetime NULL DEFAULT NULL,
  `moonsetTime` datetime NULL DEFAULT NULL,
  `precipitationProbabilityAvg` float NULL DEFAULT NULL,
  `precipitationProbabilityMax` float NULL DEFAULT NULL,
  `precipitationProbabilityMin` float NULL DEFAULT NULL,
  `pressureSurfaceLevelAvg` float NULL DEFAULT NULL,
  `pressureSurfaceLevelMax` float NULL DEFAULT NULL,
  `pressureSurfaceLevelMin` float NULL DEFAULT NULL,
  `rainAccumulationAvg` float NULL DEFAULT NULL,
  `rainAccumulationLweAvg` float NULL DEFAULT NULL,
  `rainAccumulationLweMax` float NULL DEFAULT NULL,
  `rainAccumulationLweMin` float NULL DEFAULT NULL,
  `rainAccumulationMax` float NULL DEFAULT NULL,
  `rainAccumulationMin` float NULL DEFAULT NULL,
  `rainAccumulationSum` float NULL DEFAULT NULL,
  `rainIntensityAvg` float NULL DEFAULT NULL,
  `rainIntensityMax` float NULL DEFAULT NULL,
  `rainIntensityMin` float NULL DEFAULT NULL,
  `sleetAccumulationAvg` float NULL DEFAULT NULL,
  `sleetAccumulationLweAvg` float NULL DEFAULT NULL,
  `sleetAccumulationLweMax` float NULL DEFAULT NULL,
  `sleetAccumulationLweMin` float NULL DEFAULT NULL,
  `sleetAccumulationLweSum` float NULL DEFAULT NULL,
  `sleetAccumulationMax` float NULL DEFAULT NULL,
  `sleetAccumulationMin` float NULL DEFAULT NULL,
  `sleetIntensityAvg` float NULL DEFAULT NULL,
  `sleetIntensityMax` float NULL DEFAULT NULL,
  `sleetIntensityMin` float NULL DEFAULT NULL,
  `snowAccumulationAvg` float NULL DEFAULT NULL,
  `snowAccumulationLweAvg` float NULL DEFAULT NULL,
  `snowAccumulationLweMax` float NULL DEFAULT NULL,
  `snowAccumulationLweMin` float NULL DEFAULT NULL,
  `snowAccumulationLweSum` float NULL DEFAULT NULL,
  `snowAccumulationMax` float NULL DEFAULT NULL,
  `snowAccumulationMin` float NULL DEFAULT NULL,
  `snowAccumulationSum` float NULL DEFAULT NULL,
  `snowIntensityAvg` float NULL DEFAULT NULL,
  `snowIntensityMax` float NULL DEFAULT NULL,
  `snowIntensityMin` float NULL DEFAULT NULL,
  `sunriseTime` datetime NULL DEFAULT NULL,
  `sunsetTime` datetime NULL DEFAULT NULL,
  `temperatureApparentAvg` float NULL DEFAULT NULL,
  `temperatureApparentMax` float NULL DEFAULT NULL,
  `temperatureApparentMin` float NULL DEFAULT NULL,
  `temperatureAvg` float NULL DEFAULT NULL,
  `temperatureMax` float NULL DEFAULT NULL,
  `temperatureMin` float NULL DEFAULT NULL,
  `uvHealthConcernAvg` int NULL DEFAULT NULL,
  `uvHealthConcernMax` int NULL DEFAULT NULL,
  `uvHealthConcernMin` int NULL DEFAULT NULL,
  `uvIndexAvg` int NULL DEFAULT NULL,
  `uvIndexMax` int NULL DEFAULT NULL,
  `uvIndexMin` int NULL DEFAULT NULL,
  `visibilityAvg` float NULL DEFAULT NULL,
  `visibilityMax` float NULL DEFAULT NULL,
  `visibilityMin` float NULL DEFAULT NULL,
  `weatherCodeMax` int NULL DEFAULT NULL,
  `weatherCodeMin` int NULL DEFAULT NULL,
  `windDirectionAvg` float NULL DEFAULT NULL,
  `windGustAvg` float NULL DEFAULT NULL,
  `windGustMax` float NULL DEFAULT NULL,
  `windGustMin` float NULL DEFAULT NULL,
  `windSpeedAvg` float NULL DEFAULT NULL,
  `windSpeedMax` float NULL DEFAULT NULL,
  `windSpeedMin` float NULL DEFAULT NULL,
  `create_at` datetime NULL DEFAULT NULL,
  `create_by` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `update_by` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_weather_code_max`(`weatherCodeMax` ASC) USING BTREE,
  INDEX `fk_weather_code_min`(`weatherCodeMin` ASC) USING BTREE,
  INDEX `fk_uv_health_concern_max`(`uvHealthConcernMax` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Procedure structure for getDataAggerateCurrentDate
-- ----------------------------
DROP PROCEDURE IF EXISTS `getDataAggerateCurrentDate`;
delimiter ;;
CREATE PROCEDURE `getDataAggerateCurrentDate`()
BEGIN
	#Routine body goes here...
	SELECT * FROM aggregate_weatherdata WHERE DATE(aggregate_weatherdata.create_at)= CURRENT_DATE;

END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for tranformFactToAggregate
-- ----------------------------
DROP PROCEDURE IF EXISTS `tranformFactToAggregate`;
delimiter ;;
CREATE PROCEDURE `tranformFactToAggregate`(IN date DATE)
BEGIN
    INSERT INTO aggregate_weatherdata
    SELECT NULL,f.forecastday,f.dewPointAvg,f.humidityAvg,f.moonriseTime,f.moonsetTime,f.precipitationProbabilityMax,f.pressureSurfaceLevelAvg,f.rainAccumulationAvg,f.rainAccumulationLweAvg,f.                rainAccumulationLweMax,f.rainAccumulationLweMin,f.rainAccumulationSum,f.sunriseTime,f.sunsetTime,f.temperatureApparentAvg,f.temperatureApparentMax,f.temperatureApparentMin,f.temperatureAvg,f.temperatureMax,f.temperatureMin,f.uvHealthConcernMax,f.uvIndexMax,f.visibilityAvg,d.status,d.link_icon,f.windDirectionAvg,f.windGustAvg,f.windGustMax,f.windSpeedAvg,f.windSpeedMax,f.create_at,'phung',f.create_by,f.update_by 
    FROM fact_weather f JOIN dim_weather_code d WHERE f.weatherCodeMax = d.code;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
