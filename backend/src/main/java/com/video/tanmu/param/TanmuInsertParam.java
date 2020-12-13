package com.video.tanmu.param;

import lombok.Data;

@Data
public class TanmuInsertParam {
    private String av;
    /**
     * 播放来源
     */
    private String fromName;

    /**
     * 选集
     */
    private String playName;

    /**
     * 弹幕内容
     */
    private String content;

    /**
     * 弹幕时间
     */
    private Integer currentTime;

}
