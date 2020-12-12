package com.video.tanmu.vo;

import lombok.Data;

import java.util.List;

@Data
public class VideoPlayGroup {
    /**
     * 播放来源
     */
    private String fromName;

    /**
     * 选集列表
     */
    private List<VideoPlayUrlVo> videoPlayUrlVoList;

}
