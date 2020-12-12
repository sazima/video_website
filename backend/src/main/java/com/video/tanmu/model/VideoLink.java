package com.video.tanmu.model;

import java.io.Serializable;
import lombok.Data;

@Data
public class VideoLink implements Serializable {
    private Integer id;

    private Integer videoId;

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

    private static final long serialVersionUID = 1L;
}