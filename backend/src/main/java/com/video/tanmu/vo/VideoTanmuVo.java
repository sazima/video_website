package com.video.tanmu.vo;

import lombok.Data;

@Data
public class VideoTanmuVo {
    /**
     * 弹幕内容
     */
    private String content;
    /**
     * 样式
     */
    private String style;
    /**
     * 弹幕时间
     */
    private Double currentTime;

    /**
     * 时间取整数
     */
    private Integer currentTimeInt;

    public VideoTanmuVo() {}
    public VideoTanmuVo(String content, Double currentTime, Integer currentTimeInt) {
        this.content = content;
        this.currentTime = currentTime;
        this.currentTimeInt = currentTimeInt;
    }
}
