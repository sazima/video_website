package com.video.tanmu.vo;

import lombok.Data;

import java.io.Serializable;

@Data
public class TypeVo implements Serializable {
    private Integer id;
    private String name;
    private Integer parentType;
    private Integer sort;
}
