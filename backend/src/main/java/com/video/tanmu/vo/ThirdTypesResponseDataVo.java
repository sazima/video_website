package com.video.tanmu.vo;

import lombok.Data;

import java.util.List;

@Data
public class ThirdTypesResponseDataVo {

    @Data
    static public class TypeInfoVo{
        private Integer id;
        private String name;

    }
    private List<TypeInfoVo> data;
}
