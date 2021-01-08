package com.video.tanmu.model;

import lombok.Data;

import java.io.Serializable;

/**
 * video_tanmu
 * @author 
 */
@Data
public class VideoTanmuModel implements Serializable {
    private Integer id;

    private Integer videoLinkId;
    private Integer videoId;

    /**
     * 弹幕内容
     */
    private String content;

    /**
     * 样式
     */
    private String style;

    /**
     * 播放来源
     */
    private String fromName;

    /**
     * 选集
     */
    private String playName;

    /**
     * 播放url
     */
    private String playUrl;

    /**
     * 弹幕时间
     */
    private Double currentTime;

    /**
     * 时间取整数
     */
    private Integer currentTimeInt;

    private static final long serialVersionUID = 1L;
}