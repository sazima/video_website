package com.video.tanmu.vo;

import lombok.Data;

import java.util.List;
import java.util.Map;

@Data
public class ThirdCollectionApiVo {
    @Data
    public static class BindIdVo {
        private Integer systemId;
        private Integer apiId;
        private String typeName;
        private String apiName;
    }
    private Integer id;

    /**
     * api 链接
     */
    private String url;

    /**
     * 唯一标志
     */
    private String key;

    /**
     * 名称,显示在页面上
     */
    private String name;

    /**
     * 分类绑定, api的分类对应的系统分类
     */
    private List<BindIdVo> bindId;
}
