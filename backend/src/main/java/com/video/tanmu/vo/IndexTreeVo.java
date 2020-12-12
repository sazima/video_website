package com.video.tanmu.vo;

import lombok.Data;

import java.util.List;

@Data
public class IndexTreeVo {
    private List<TypeVo> typeVoList;
    private List<TypeWithVideoListVo> typeWithVideoListVoList;
}
