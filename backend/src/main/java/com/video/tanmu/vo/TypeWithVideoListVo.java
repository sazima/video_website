package com.video.tanmu.vo;

import lombok.Data;

import java.io.Serializable;
import java.util.List;

@Data
public class TypeWithVideoListVo implements Serializable {
    private String typeName;
    private Integer typeId;
    private List<VideoListVo> videoListVos;
}
