package com.video.tanmu.vo;

import lombok.Data;

import java.util.List;

@Data
public class VideoPlayUrlVo {
    @Data
    public static class  Url {
        private String src;
        private String type = "application/x-mpegURL";
        private String label;
        private Boolean selected = false;
        public Url(String src, String label, boolean selected) {
            this.src = src;
            this.label = label;
            this.selected = selected;
        }
    }

    private List<Url> url;
    private String name;

    public VideoPlayUrlVo() {}

    public VideoPlayUrlVo(String name, List<Url> url) {
        this.url = url;
        this.name = name;
    }
}
