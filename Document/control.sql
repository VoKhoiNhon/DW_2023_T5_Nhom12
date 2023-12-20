/*
 Navicat Premium Data Transfer

 Source Server         : aaaaa
 Source Server Type    : MySQL
 Source Server Version : 100432 (10.4.32-MariaDB)
 Source Host           : localhost:3306
 Source Schema         : control

 Target Server Type    : MySQL
 Target Server Version : 100432 (10.4.32-MariaDB)
 File Encoding         : 65001

 Date: 20/12/2023 20:33:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for control_data_file
-- ----------------------------
DROP TABLE IF EXISTS `control_data_file`;
CREATE TABLE `control_data_file`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_config` int NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `row_count` bigint NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `data_range_from` datetime NULL DEFAULT NULL,
  `data_range_to` datetime NULL DEFAULT NULL,
  `note` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `create_at` datetime NULL DEFAULT NULL,
  `update_at` datetime NULL DEFAULT NULL,
  `create_by` varchar(20) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `update_by` varchar(20) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_file_config`(`id_config` ASC) USING BTREE,
  CONSTRAINT `fk_file_config` FOREIGN KEY (`id_config`) REFERENCES `control_data_file_configs` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 53 CHARACTER SET = utf8 COLLATE = utf8_vietnamese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for control_data_file_configs
-- ----------------------------
DROP TABLE IF EXISTS `control_data_file_configs`;
CREATE TABLE `control_data_file_configs`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL,
  `src_path` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `format` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `separator` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `columns` bigint NULL DEFAULT NULL,
  `destination` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `create_at` datetime NULL DEFAULT NULL,
  `update_at` datetime NULL DEFAULT NULL,
  `create_by` varchar(20) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `update_by` varchar(20) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_vietnamese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_config` int NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL DEFAULT NULL,
  `note` text CHARACTER SET utf8 COLLATE utf8_vietnamese_ci NULL,
  `log_date` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_log_config`(`id_config` ASC) USING BTREE,
  CONSTRAINT `fk_log_config` FOREIGN KEY (`id_config`) REFERENCES `control_data_file_configs` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 252 CHARACTER SET = utf8 COLLATE = utf8_vietnamese_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Procedure structure for getConfig
-- ----------------------------
DROP PROCEDURE IF EXISTS `getConfig`;
delimiter ;;
CREATE PROCEDURE `getConfig`(IN id INT)
BEGIN
    #Routine body goes here...
SELECT * FROM control_data_file_configs WHERE id = (id);
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getControlDataFileByDate
-- ----------------------------
DROP PROCEDURE IF EXISTS `getControlDataFileByDate`;
delimiter ;;
CREATE PROCEDURE `getControlDataFileByDate`(IN p_status VARCHAR(255), IN date DATE)
BEGIN
    #Routine body goes here...
SELECT * FROM control_data_file WHERE status = p_status AND DATE(create_at) = date;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getDataFileToday
-- ----------------------------
DROP PROCEDURE IF EXISTS `getDataFileToday`;
delimiter ;;
CREATE PROCEDURE `getDataFileToday`(in status_In VARCHAR(255))
BEGIN
	#Routine body goes here...
	select * from control_data_file WHERE status = status_In;

END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for getStatus
-- ----------------------------
DROP PROCEDURE IF EXISTS `getStatus`;
delimiter ;;
CREATE PROCEDURE `getStatus`()
BEGIN
	#Routine body goes here...
	select status from control_data_file WHERE Date(control_data_file.update_at)= CURRENT_DATE;

END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updateStatusDataFile
-- ----------------------------
DROP PROCEDURE IF EXISTS `updateStatusDataFile`;
delimiter ;;
CREATE PROCEDURE `updateStatusDataFile`(IN id_data_file INT, IN status_in VARCHAR(255))
BEGIN
    #Routine body goes here...
UPDATE control_data_file SET status = status_in WHERE id = id_data_file;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for writeLog
-- ----------------------------
DROP PROCEDURE IF EXISTS `writeLog`;
delimiter ;;
CREATE PROCEDURE `writeLog`(IN id_config_in INT, IN status_in VARCHAR(255), IN note_in VARCHAR(255))
BEGIN
    #Routine body goes here...
INSERT INTO log (id_config, status, note, log_date) VALUES (id_config_in, status_in, note_in,CURRENT_TIMESTAMP );
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
