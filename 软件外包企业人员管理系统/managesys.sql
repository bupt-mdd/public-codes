/*
Navicat MySQL Data Transfer

Source Server         : 111
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : managesys

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2017-05-19 16:00:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admintable
-- ----------------------------
DROP TABLE IF EXISTS `admintable`;
CREATE TABLE `admintable` (
  `adminId` varchar(20) CHARACTER SET utf8 NOT NULL,
  `password` varchar(50) CHARACTER SET utf8 NOT NULL,
  `isSuper` int(11) NOT NULL,
  PRIMARY KEY (`adminId`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of admintable
-- ----------------------------
INSERT INTO `admintable` VALUES ('admin', 'd033e22ae348aeb5660fc2140aec35850c4da997', '1');
INSERT INTO `admintable` VALUES ('admin01', 'cb0ef4c7be04ff1bf4cfcd104ef8df03251266ab', '0');
INSERT INTO `admintable` VALUES ('admin02', 'd5f3f4db6d8400f894bde2523e8247b9ff2346fb', '0');

-- ----------------------------
-- Table structure for newstable
-- ----------------------------
DROP TABLE IF EXISTS `newstable`;
CREATE TABLE `newstable` (
  `newsID` varchar(40) CHARACTER SET utf8 NOT NULL,
  `newsContent` varchar(3500) CHARACTER SET utf8 DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `location` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`newsID`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of newstable
-- ----------------------------
INSERT INTO `newstable` VALUES ('公司新建xx', '    发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货\r\n   发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货\r\n   发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货\r\n    发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货发货的数据库恢复上课就发货', '2017-04-03 09:22:20', 'upload/发的还是尽快发货.jpg');
INSERT INTO `newstable` VALUES ('xx来公司视察', '     投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹\r\n    投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹\r\n    投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹\r\n     投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹投入特肉徒儿哦徒惹', '2017-04-03 09:23:26', 'upload/图热哦突然.jpg');
INSERT INTO `newstable` VALUES ('xx攻破难题', '     发达省份身份回复即可获得是分开发达省份身份回复即可获得是分开发达省份身份回复即可获得是分开发达省份身份回复即可获得是分开发达省份身份回复即可获得是分开发达省份身份回复即可获得是分开', '2017-04-03 09:23:56', 'upload/额问问机房说的.jpg');
INSERT INTO `newstable` VALUES ('公司团建1', '    锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦锐意进取啦啦啦啦啦', '2017-04-03 09:24:26', 'upload/一如我睿翼.jpg');
INSERT INTO `newstable` VALUES ('公司团建2', '     和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方和福克斯的回访客户反馈京东方', '2017-04-03 09:24:47', 'upload/人以为我日.jpg');
INSERT INTO `newstable` VALUES ('公司团建3', '    回复肯定是分开就撒谎扣分哈哈发回复肯定是分开就撒谎扣分哈哈发回复肯定是分开就撒谎扣分哈哈发回复肯定是分开就撒谎扣分哈哈发回复肯定是分开就撒谎扣分哈哈发\r\n   回复肯定是分开就撒谎扣分哈哈发回复肯定是分开就撒谎扣分哈哈发\r\n   回复肯定是分开就撒谎扣分哈哈发', '2017-04-03 09:25:26', 'upload/女款男款的肌肤.jpg');
INSERT INTO `newstable` VALUES ('公司团建4', 'ffhgfghfhgfhgfhfghfgfghfhfghfgfhfgg', '2017-05-02 11:15:19', 'upload/fghfhgfghf.jpg');

-- ----------------------------
-- Table structure for noticetable
-- ----------------------------
DROP TABLE IF EXISTS `noticetable`;
CREATE TABLE `noticetable` (
  `noticeID` varchar(40) CHARACTER SET utf8 NOT NULL,
  `noticeContent` varchar(3500) CHARACTER SET utf8 DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`noticeID`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of noticetable
-- ----------------------------
INSERT INTO `noticetable` VALUES ('xx公司派遣通知', '      符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看\r\n     符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看\r\n       符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看\r\n       符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看符合双方开始减肥还是开机就耗费精神亢奋和辅导教师考核方式看', '2017-04-02 08:30:24');
INSERT INTO `noticetable` VALUES ('java培训通知', 'fds', '2017-04-02 11:15:24');
INSERT INTO `noticetable` VALUES ('php培训通知', '       减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的\r\n       减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的\r\n       减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的减肥的拉升阶段楼上的房间啊老费劲啊是的\r\n      减肥的拉升阶段楼上的房间啊老费劲啊是的', '2017-04-03 03:43:34');
INSERT INTO `noticetable` VALUES ('android培训通知', '       发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设\r\n       发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设\r\n       发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设\r\n       发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设发货的手机话费空间和对方接受的回复的技术开发建设', '2017-04-03 03:46:26');
INSERT INTO `noticetable` VALUES ('C语言培训通知', '       发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的\r\n       发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的\r\n       发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的发到圣诞节分厘卡撒酒疯了减肥的是精神分裂的', '2017-04-03 03:48:35');
INSERT INTO `noticetable` VALUES ('放假通知', 'hfhjdshfkjshkfjshdf', '2017-04-03 04:20:54');
INSERT INTO `noticetable` VALUES ('员工招聘通知', 'fdsfdfdsafsafasdfd', '2017-04-25 10:26:40');

-- ----------------------------
-- Table structure for outsendinftable
-- ----------------------------
DROP TABLE IF EXISTS `outsendinftable`;
CREATE TABLE `outsendinftable` (
  `outSendName` varchar(40) CHARACTER SET utf8 NOT NULL,
  `startTime` date DEFAULT NULL,
  `endTime` date DEFAULT NULL,
  `outSendContent` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `isEnd` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`outSendName`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of outsendinftable
-- ----------------------------
INSERT INTO `outsendinftable` VALUES ('fdsfdss', '2017-01-01', '2017-01-01', 'fdsdfds', 'yes');
INSERT INTO `outsendinftable` VALUES ('fdss', '2017-01-01', '2018-01-01', 'fdsssssss', 'yes');
INSERT INTO `outsendinftable` VALUES ('项目编写', '2017-01-01', '2017-01-01', '房贷首付啦啦啦', 'yes');
INSERT INTO `outsendinftable` VALUES ('xx', '2017-01-01', '2017-01-01', '拉布拉布拉布啦啦啦', 'yes');
INSERT INTO `outsendinftable` VALUES ('空调系统同', '2017-01-01', '2017-01-01', '啦啦啦', 'yes');
INSERT INTO `outsendinftable` VALUES ('lalali', '2017-01-01', '2017-01-01', 'fsdddddddrewerwhhhhh', 'yes');
INSERT INTO `outsendinftable` VALUES ('hhhh', '2017-01-01', '2017-01-01', 'fdsdsfdsfeeeehhhhhhh', 'yes');
INSERT INTO `outsendinftable` VALUES ('范德萨', '2017-01-01', '2017-01-01', '范德萨', 'yes');
INSERT INTO `outsendinftable` VALUES ('trtrtetertre', '2017-01-01', '2017-01-01', 'terttretreeeefff', 'yes');
INSERT INTO `outsendinftable` VALUES ('xx公司管理系统开发', '2017-01-01', '2017-01-01', '风华绝代是宽恕对方和封建时代和开发商都是', 'no');
INSERT INTO `outsendinftable` VALUES ('xx公司桌面app开发', '2017-01-01', '2017-01-01', '房地网粉红色的伤口就合服的事', 'no');
INSERT INTO `outsendinftable` VALUES ('fds外包项目', '2017-01-01', '2017-01-01', '发士大夫十分', 'no');

-- ----------------------------
-- Table structure for resourcetable
-- ----------------------------
DROP TABLE IF EXISTS `resourcetable`;
CREATE TABLE `resourcetable` (
  `resourceID` varchar(30) CHARACTER SET utf8 NOT NULL,
  `location` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`resourceID`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of resourcetable
-- ----------------------------
INSERT INTO `resourcetable` VALUES ('培训申请表', 'download/房贷首付.docx');
INSERT INTO `resourcetable` VALUES ('派遣申请表', 'download/fdsf.docx');
INSERT INTO `resourcetable` VALUES ('奖金申请表', 'download/犯得上示范点是否是.docx');
INSERT INTO `resourcetable` VALUES ('先进个人申请表', 'download/热望热望.docx');
INSERT INTO `resourcetable` VALUES ('先进团队申请表', 'download/犹太人头痛医头.docx');
INSERT INTO `resourcetable` VALUES ('项目申请表', 'download/恢复共和国.docx');
INSERT INTO `resourcetable` VALUES ('fsdfdsfsdfds', 'download/fsdfdsfsdfds.docx');
INSERT INTO `resourcetable` VALUES ('11111', 'download/11111.docx');

-- ----------------------------
-- Table structure for resumetable
-- ----------------------------
DROP TABLE IF EXISTS `resumetable`;
CREATE TABLE `resumetable` (
  `name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `dateOfBirth` date NOT NULL,
  `IDNumber` varchar(30) CHARACTER SET utf8 NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8 NOT NULL,
  `phoneNumber` varchar(15) CHARACTER SET utf8 NOT NULL,
  `QQNumber` varchar(14) CHARACTER SET utf8 DEFAULT NULL,
  `email` varchar(40) CHARACTER SET utf8 DEFAULT NULL,
  `awards` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `eduBackground` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `practiceExperience` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `personalAbility` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`IDNumber`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of resumetable
-- ----------------------------
INSERT INTO `resumetable` VALUES ('马桂', '2017-01-12', '789456123321654987', 'male', '4567891233', '', '', '', '', '', '');
INSERT INTO `resumetable` VALUES ('唐躺', '2017-01-01', '456789321147852963', 'male', '45454545455', '', '', '', '', '', '');

-- ----------------------------
-- Table structure for traininginftable
-- ----------------------------
DROP TABLE IF EXISTS `traininginftable`;
CREATE TABLE `traininginftable` (
  `trainingName` varchar(40) CHARACTER SET utf8 NOT NULL,
  `startTime` date DEFAULT NULL,
  `endTime` date DEFAULT NULL,
  `trainingContent` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `isEnd` varchar(4) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`trainingName`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of traininginftable
-- ----------------------------
INSERT INTO `traininginftable` VALUES ('fds', '2017-01-01', '2017-01-01', 'fdsfds', 'yes');
INSERT INTO `traininginftable` VALUES ('sdf', '2017-01-01', '2017-01-01', 'fdssss', 'yes');
INSERT INTO `traininginftable` VALUES ('tretre', '2017-01-01', '2017-01-01', 'tret', 'yes');
INSERT INTO `traininginftable` VALUES ('java培训', '2017-01-01', '2017-01-01', 'java技术原理', 'yes');
INSERT INTO `traininginftable` VALUES ('c培训', '2017-01-01', '2017-01-01', '基础知识', 'yes');
INSERT INTO `traininginftable` VALUES ('Clalala', '2017-01-01', '2017-01-01', 'fdsfs', 'yes');
INSERT INTO `traininginftable` VALUES ('fdsdfsfsfsd', '2017-01-04', '2017-01-19', 'fdsffffff', 'yes');
INSERT INTO `traininginftable` VALUES ('hhhh', '2017-01-01', '2017-01-01', 'hhh', 'yes');
INSERT INTO `traininginftable` VALUES ('pascal语言培训', '2017-01-01', '2017-01-01', '基础知识的运用和掌握', 'yes');
INSERT INTO `traininginftable` VALUES ('hfdjhdsjkdhfk', '2017-01-01', '2017-01-01', 'fhdsjkdfskfhfff', 'yes');
INSERT INTO `traininginftable` VALUES ('java培训（一）', '2017-06-01', '2017-11-01', '掌握基本语法\r\n多线程的应用\r\n图形界面的设计', 'no');

-- ----------------------------
-- Table structure for userinftable
-- ----------------------------
DROP TABLE IF EXISTS `userinftable`;
CREATE TABLE `userinftable` (
  `userId` varchar(20) CHARACTER SET utf8 NOT NULL,
  `password` varchar(50) CHARACTER SET utf8 NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `IDNumber` varchar(30) CHARACTER SET utf8 NOT NULL,
  `dateOfBirth` date NOT NULL,
  `phoneNumber` varchar(15) CHARACTER SET utf8 NOT NULL,
  `gender` varchar(10) CHARACTER SET utf8 NOT NULL,
  `QQNumber` varchar(14) CHARACTER SET utf8 DEFAULT NULL,
  `email` varchar(40) CHARACTER SET utf8 DEFAULT NULL,
  `awards` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `eduBackground` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `practiceExperience` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `personalAbility` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `isBusy` int(11) DEFAULT NULL,
  `interviewEvaluation` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of userinftable
-- ----------------------------
INSERT INTO `userinftable` VALUES ('20170011', '416f8f6e105370e7b9d0fd983141f00b613477f8', 'thzzaa', '1233', '2017-01-02', '1231233', 'male', '4324234322', 'fdsff@123.com', 'fdsfsd\r\nfdsfsd', 'gf\r\ngfd', 'hgf\r\nhff', 'ytr\r\nyt\r\nty', '1', '房价肯定是分开时间发');
INSERT INTO `userinftable` VALUES ('20170012', 'db00e4fdc8a6d8fc749a23649c9ec9343051ec47', 'hgf', '654', '2016-12-15', '654', 'male', '', '', 'hgfs', 'hjhk\r\nhg', 'hj\r\ntre', 'kll\r\nhgh', '1', 'no');
INSERT INTO `userinftable` VALUES ('20170013', 'fea7f657f56a2a448da7d4b535ee5e279caf3d9a', 'ggg', '2222', '2017-01-01', '2222', 'male', '', '', '', '', '', '', '1', 'no');
INSERT INTO `userinftable` VALUES ('20170014', '761ee866d554db1c7582326a910fac8b9764c345', 'ffffffdsfs', '3333333', '2017-01-01', '333333333', 'male', '', '', '', '', '', '', '1', 'no');
INSERT INTO `userinftable` VALUES ('20170015', '92f2fd99879b0c2466ab8648afb63c49032379c1', '5545', '4444', '2017-01-01', '3323', 'male', '', '', 'hgf\r\ngdf', 'hdff\r\nfds\r\nfd', 'jhj\r\njhj\r\nh', 'fds\r\nfds', '1', 'no');
INSERT INTO `userinftable` VALUES ('20170016', 'c08d9955148bc0199789922ca232a77b69003980', 'fdsdafa', '875', '2017-01-01', '45', 'male', '', '', '', '', '', '', '1', 'no');
INSERT INTO `userinftable` VALUES ('20170017', '44ff62391064d611d13cc79f527453b0099b4cec', '马冬冬', '1231232131', '2017-01-01', '1231232', 'male', '151515', 'mdd@123.com', '拉布拉布拉布\r\n拉布拉布拉布\r\n拉布拉布拉布', '拉布拉布拉布\r\n拉布拉布拉布\r\n拉布拉布拉布', '就是很费解的是\r\n附近的说法是', '花费的时间客户反馈\r\n发到手机开发还是快点', '1', 'no');
INSERT INTO `userinftable` VALUES ('20170018', '7e357d93939665741933f8ec66e1627cced787cc', '刘训', '123456789789456123', '2017-01-01', '12345678', 'male', '1212121212', 'liuxvn@163.com', '2013-2015年，获得优秀创业者称号1\r\n2013-2015年，获得优秀创业者称号2\r\n2013-2015年，获得优秀创业者称号3', '2013-2015年，获得xxx大学博士学位', '2013-2015年，在xx公司实习\r\n2013-2015年，在nn公司当设计总监\r\n2013-2015年，在mm公司当技术总监', '可以熟练操作办公软件1\r\n可以熟练操作办公软件2\r\n可以熟练操作办公软件3', '1', 'no');

-- ----------------------------
-- Table structure for usertooutsend
-- ----------------------------
DROP TABLE IF EXISTS `usertooutsend`;
CREATE TABLE `usertooutsend` (
  `userId` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `outSendName` varchar(40) CHARACTER SET utf8 DEFAULT NULL,
  `interviewEvaluation` varchar(255) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of usertooutsend
-- ----------------------------
INSERT INTO `usertooutsend` VALUES ('20170012', 'fdss', 'no');
INSERT INTO `usertooutsend` VALUES ('20170013', 'fdsfdss', 'no');
INSERT INTO `usertooutsend` VALUES ('20170015', 'fdsfdss', 'no');
INSERT INTO `usertooutsend` VALUES ('20170011', 'fdsfdss', 'ffdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞fdjsfjsljfslfj将阿飞djsfjsljfslfj将阿飞');
INSERT INTO `usertooutsend` VALUES ('20170014', 'fdss', 'no');
INSERT INTO `usertooutsend` VALUES ('20170012', '项目编写', 'no');
INSERT INTO `usertooutsend` VALUES ('20170013', '项目编写', 'no');
INSERT INTO `usertooutsend` VALUES ('20170014', '项目编写', 'no');
INSERT INTO `usertooutsend` VALUES ('20170015', '项目编写', 'no');
INSERT INTO `usertooutsend` VALUES ('20170011', 'xx', '加菲你打算开发');
INSERT INTO `usertooutsend` VALUES ('20170012', 'xx', 'no');
INSERT INTO `usertooutsend` VALUES ('20170013', 'xx', 'no');
INSERT INTO `usertooutsend` VALUES ('20170014', 'xx', 'no');
INSERT INTO `usertooutsend` VALUES ('20170015', 'xx', 'no');
INSERT INTO `usertooutsend` VALUES ('20170011', '空调系统同', '发的好时机开发商的');
INSERT INTO `usertooutsend` VALUES ('20170014', '空调系统同', 'no');
INSERT INTO `usertooutsend` VALUES ('20170012', '空调系统同', 'no');
INSERT INTO `usertooutsend` VALUES ('20170013', 'hhhh', 'no');
INSERT INTO `usertooutsend` VALUES ('20170014', 'hhhh', 'no');
INSERT INTO `usertooutsend` VALUES ('20170015', 'hhhh', 'no');
INSERT INTO `usertooutsend` VALUES ('20170011', '项目编写', '表现良好，团队意识很强，善于与人沟通\r\n善于表达，创新意识强');
INSERT INTO `usertooutsend` VALUES ('20170017', '范德萨', 'no');
INSERT INTO `usertooutsend` VALUES ('20170015', 'trtrtetertre', 'no');
INSERT INTO `usertooutsend` VALUES ('20170016', 'trtrtetertre', 'no');
INSERT INTO `usertooutsend` VALUES ('20170011', 'trtrtetertre', 'no');
INSERT INTO `usertooutsend` VALUES ('20170012', 'trtrtetertre', 'no');
INSERT INTO `usertooutsend` VALUES ('20170015', 'xx公司管理系统开发', 'no');
INSERT INTO `usertooutsend` VALUES ('20170016', 'xx公司管理系统开发', 'no');
INSERT INTO `usertooutsend` VALUES ('20170014', 'fds外包项目', 'no');
INSERT INTO `usertooutsend` VALUES ('20170017', 'fds外包项目', 'no');
INSERT INTO `usertooutsend` VALUES ('20170011', 'xx公司管理系统开发', 'no');
INSERT INTO `usertooutsend` VALUES ('20170013', 'xx公司桌面app开发', 'no');
INSERT INTO `usertooutsend` VALUES ('20170012', 'xx公司管理系统开发', 'no');
INSERT INTO `usertooutsend` VALUES ('20170018', 'xx公司管理系统开发', 'no');

-- ----------------------------
-- Table structure for usertotraining
-- ----------------------------
DROP TABLE IF EXISTS `usertotraining`;
CREATE TABLE `usertotraining` (
  `userId` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `trainingName` varchar(40) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=gbk;

-- ----------------------------
-- Records of usertotraining
-- ----------------------------
INSERT INTO `usertotraining` VALUES ('20170015', 'tretre');
INSERT INTO `usertotraining` VALUES ('20170014', 'sdf');
INSERT INTO `usertotraining` VALUES ('20170013', 'sdf');
INSERT INTO `usertotraining` VALUES ('20170012', 'fds');
INSERT INTO `usertotraining` VALUES ('20170011', 'fds');
INSERT INTO `usertotraining` VALUES ('20170011', 'tretre');
INSERT INTO `usertotraining` VALUES ('20170012', 'tretre');
INSERT INTO `usertotraining` VALUES ('20170013', 'tretre');
INSERT INTO `usertotraining` VALUES ('20170014', 'tretre');
INSERT INTO `usertotraining` VALUES ('20170011', 'java培训');
INSERT INTO `usertotraining` VALUES ('20170012', 'java培训');
INSERT INTO `usertotraining` VALUES ('20170013', 'java培训');
INSERT INTO `usertotraining` VALUES ('20170014', 'java培训');
INSERT INTO `usertotraining` VALUES ('20170015', 'java培训');
INSERT INTO `usertotraining` VALUES ('20170013', 'Clalala');
INSERT INTO `usertotraining` VALUES ('20170012', 'Clalala');
INSERT INTO `usertotraining` VALUES ('20170015', 'c培训');
INSERT INTO `usertotraining` VALUES ('20170014', 'c培训');
INSERT INTO `usertotraining` VALUES ('20170011', 'c培训');
INSERT INTO `usertotraining` VALUES ('20170016', 'Clalala');
INSERT INTO `usertotraining` VALUES ('20170011', 'hhhh');
INSERT INTO `usertotraining` VALUES ('20170016', 'hhhh');
INSERT INTO `usertotraining` VALUES ('20170017', 'pascal语言培训');
INSERT INTO `usertotraining` VALUES ('20170011', 'hfdjhdsjkdhfk');
INSERT INTO `usertotraining` VALUES ('20170012', 'hfdjhdsjkdhfk');
INSERT INTO `usertotraining` VALUES ('20170013', 'hfdjhdsjkdhfk');
INSERT INTO `usertotraining` VALUES ('20170014', 'hfdjhdsjkdhfk');
INSERT INTO `usertotraining` VALUES ('20170017', 'hfdjhdsjkdhfk');
