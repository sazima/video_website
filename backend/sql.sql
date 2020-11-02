CREATE TABLE mac_tanmu
(
    tanmu_id           INT(11) PRIMARY KEY AUTO_INCREMENT,
    vod_id             INT(11) COMMENT '视频id',
    play_url           VARCHAR(255) COMMENT '播放链接',
    content            VARCHAR(255),
    `current_time`     FLOAT(11) COMMENT '时间',
    `current_time_int` INT(11) COMMENT '时间取整',
    `play_line_name` VARCHAR(255) COMMENT '名称, 比如播放地址1',
    `play_name` VARCHAR(255) COMMENT '链接名称, 比如第一集',
    `styles`           TEXT COMMENT '样式',
    user_id            INT(11),
    create_time        DATETIME DEFAULT now(),
    INDEX (vod_id)
)

