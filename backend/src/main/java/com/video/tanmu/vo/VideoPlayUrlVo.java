package com.video.tanmu.vo;

import lombok.Data;

@Data
public class VideoPlayUrlVo {

    private String url;
    private String name;

    public VideoPlayUrlVo() {}
    public VideoPlayUrlVo(String name, String url) {
        this.url = url;
        this.name = name;
    }
}
