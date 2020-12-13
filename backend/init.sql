CREATE  DATABASE tanmu_video DEFAULT charset utf8mb4;
use tanmu_video;

CREATE TABLE type
(
    id          int(11) PRIMARY KEY AUTO_INCREMENT,
    name        varchar(255) DEFAULT '' COMMENT '名称',
    parent_type int(11)      DEFAULT 0 COMMENT '父级分类',
    sort        int(11)      DEFAULT 0 COMMENT '排序'
);

CREATE TABLE video
(
    id       int(11) PRIMARY KEY AUTO_INCREMENT,
    type_id1 int(11)      DEFAULT 0 COMMENT '分类1',
    type_id2 int(11)      DEFAULT 0,
    name     varchar(255) DEFAULT '' COMMENT '名称',
    picture  varchar(255) DEFAULT '' COMMENT '图片',
    content  text COMMENT '简介内容',
    random_id varchar(255)  COMMENT '随机id'    DEFAULT 0,
    update_time int(11) default 0  COMMENT '更新时间'
);

CREATE TABLE video_link
(
    id        int(11) PRIMARY KEY AUTO_INCREMENT,
    video_id  int(11) NOT NULL,
    from_name varchar(255) DEFAULT '播放地址1' COMMENT '播放来源',
    play_name varchar(255) DEFAULT '第一集' COMMENT '选集',
    play_url  varchar(255) DEFAULT '' COMMENT '播放url'
);

CREATE TABLE video_tanmu
(
    id            int(11) PRIMARY KEY AUTO_INCREMENT,
    video_link_id int(11) NOT NULL,
    video_id int(11) NOT NULL,
    from_name varchar(255) DEFAULT '播放地址1' COMMENT '播放来源',
    play_name varchar(255) DEFAULT '第一集' COMMENT '选集',
    play_url  varchar(255) DEFAULT '' COMMENT '播放url',
    `current_time` float(5, 2) DEFAULT 0 COMMENT '弹幕时间',
    current_time_int int(11) DEFAULT 0 COMMENT '时间取整数',
    content       varchar(255) DEFAULT '' COMMENT '弹幕内容',
    style         varchar(255) DEFAULT '' COMMENT '样式'
);

