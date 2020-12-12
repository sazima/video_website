package com.video.tanmu.vo;

import lombok.Data;

@Data
public class TypeVo {
    private Integer id;
    private String name;
    private Integer parentType;
    private Integer sort;
}
