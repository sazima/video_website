package com.video.tanmu.Redis;

import com.video.tanmu.param.VideoQueryParam;

public class VideoKey {
    public static String getVideoByAvKey(String av) {
        return "videoByAv::" + av;
    }

    public static String getTotalByQueryParam(VideoQueryParam videoQueryParam) {
        return "kw::" + videoQueryParam.getKw() + "typeId::" + videoQueryParam.getTypeId();
    }
}
