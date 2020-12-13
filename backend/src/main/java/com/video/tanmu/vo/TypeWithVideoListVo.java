package com.video.tanmu.vo;

import lombok.Data;

import java.util.Date;
import java.util.List;

@Data
public class TypeWithVideoListVo {
    private String typeName;
    private Integer typeId;
    private List<VideoListVo> videoListVos;
}
