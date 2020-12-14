package com.video.tanmu.param;

import lombok.Data;

@Data
public class PageParam {
    private Integer page = 1;
    private Integer pageSize = 15;

    public Integer getOffset() {
        return (this.page - 1) * pageSize;
    }
}
