package com.video.tanmu.param;

import lombok.Data;

@Data
public class TanmuQueryParam {

    private String av;

    /**
     * 来源
     */
    private String fromName;
    /**
     * 选集
     */
    private String playName;
}
