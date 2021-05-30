package com.video.tanmu.model;

import java.io.Serializable;
import lombok.Data;

/**
 * third_collection_api
 * @author 
 */
@Data
public class ThirdCollectionApiModel implements Serializable {
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
     * 分类绑定
     */
    private String bindId;

    private static final long serialVersionUID = 1L;
}