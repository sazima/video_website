CREATE DATABASE tanmu_video DEFAULT CHARSET utf8mb4;
USE tanmu_video;

CREATE TABLE type
(
    id          INT(11) PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(255) DEFAULT '' COMMENT '名称',
    parent_type INT(11)      DEFAULT 0 COMMENT '父级分类',
    sort        INT(11)      DEFAULT 0 COMMENT '排序'
);

CREATE TABLE video
(
    id          INT(11) PRIMARY KEY AUTO_INCREMENT,
    type_id1    INT(11)                     DEFAULT 0 COMMENT '分类1',
    type_id2    INT(11)                     DEFAULT 0,
    name        VARCHAR(255)                DEFAULT '' COMMENT '名称',
    av          VARCHAR(255)                DEFAULT '' COMMENT '名称',
    picture     VARCHAR(255)                DEFAULT '' COMMENT '图片',
    content     TEXT COMMENT '简介内容',
    random_id   VARCHAR(255) COMMENT '随机id' DEFAULT 0,
    update_time INT(11)                     DEFAULT 0 COMMENT '更新时间'
);

ALTER TABLE `video`
    ADD INDEX av (`av`);
ALTER TABLE `video`
    ADD INDEX type_id1 (`type_id1`);
ALTER TABLE `video`
    ADD INDEX type_id2 (`type_id2`);
CREATE TABLE video_link
(
    id        INT(11) PRIMARY KEY AUTO_INCREMENT,
    video_id  INT(11) NOT NULL,
    from_name VARCHAR(255) DEFAULT '播放地址1' COMMENT '播放来源',
    play_name VARCHAR(255) DEFAULT '第一集' COMMENT '选集',
    play_url  VARCHAR(255) DEFAULT '' COMMENT '播放url'
);
ALTER TABLE `video_link`
    ADD INDEX video_id (`video_id`);
ALTER TABLE `video_link`
    ADD INDEX from_name (`from_name`);
ALTER TABLE `video_link`
    ADD INDEX play_name (`play_name`);

CREATE TABLE video_tanmu
(
    id               INT(11) PRIMARY KEY AUTO_INCREMENT,
    video_link_id    INT(11) NOT NULL,
    video_id         INT(11) NOT NULL,
    from_name        VARCHAR(255) DEFAULT '播放地址1' COMMENT '播放来源',
    play_name        VARCHAR(255) DEFAULT '第一集' COMMENT '选集',
    play_url         VARCHAR(255) DEFAULT '' COMMENT '播放url',
    `current_time`   FLOAT(5, 2)  DEFAULT 0 COMMENT '弹幕时间',
    current_time_int INT(11)      DEFAULT 0 COMMENT '时间取整数',
    content          VARCHAR(255) DEFAULT '' COMMENT '弹幕内容',
    style            VARCHAR(255) DEFAULT '' COMMENT '样式'
);
ALTER TABLE `video_tanmu`
    ADD INDEX video_id (`video_id`);
ALTER TABLE `video_tanmu`
    ADD INDEX from_name (`from_name`);
ALTER TABLE `video_tanmu`
    ADD INDEX play_name (`play_name`);
ALTER TABLE `video_tanmu`
    ADD INDEX video_link_id (`video_link_id`);



CREATE TABLE user
(
    id        INT(11) PRIMARY KEY AUTO_INCREMENT,
    nick_name VARCHAR(255) DEFAULT '' COMMENT '昵称',
    email     VARCHAR(255) DEFAULT '' COMMENT '邮箱',
    picture   VARCHAR(255) DEFAULT '' COMMENT '头像',
    password  VARCHAR(255) NOT NULL COMMENT '密码',
    add_time  int(11)      DEFAULT 0,
    status    INT(11)      DEFAULT 0 COMMENT '状态'

);

# 用户收藏
create table user_favorite
(
    id         INT(11) PRIMARY KEY AUTO_INCREMENT,
    user_id    int(11) not null comment '用户id',
    av   varchar(255) not null comment '视频av号码',
    video_name varchar(255) default '' comment '视频名称',
    add_time int(11) default 0 comment '收藏时间'
)
