package com.video.tanmu.vo;

import lombok.Data;

import java.io.Serializable;
import java.util.List;

@Data
public class IndexTreeVo implements Serializable {
    private List<TypeVo> typeVoList;
    private List<TypeWithVideoListVo> typeWithVideoListVoList;
}
