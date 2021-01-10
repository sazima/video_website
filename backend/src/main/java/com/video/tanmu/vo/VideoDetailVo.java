package com.video.tanmu.vo;

import com.sun.corba.se.impl.ior.iiop.IIOPProfileTemplateImpl;
import lombok.Data;

import java.util.List;

@Data
public class VideoDetailVo {
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
     * 简介内容
     */
    private String content;
    /**
     * av
     */
    private String av;

    /**
     * 播放来源列表
     */
    private List<VideoPlayGroup> videoPlayGroupList;
    /**
     * 代理服务器
     */
    private List<String> proxyServicePrefixList;
}
