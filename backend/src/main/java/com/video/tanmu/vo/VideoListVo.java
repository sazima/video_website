package com.video.tanmu.vo;

import lombok.Data;

@Data
public class VideoListVo {
    /**
     * 分类1
     */
    private Integer typeId1;

    private Integer typeId2;

    /**
     * 名称
     */
    private String name;

    /**
     * 图片
     */
    private String picture;
    /**
     * av
     */
    private String av;

}
