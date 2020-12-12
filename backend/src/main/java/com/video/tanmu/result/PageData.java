package com.video.tanmu.result;

import com.github.pagehelper.PageInfo;
import lombok.Data;

import java.util.List;

@Data
public class PageData<T> {
    private long total;
    private List<T> list;
    public PageData() {
    }
    public PageData(long total, List<T> list) {
        this.total = total;
        this.list = list;
    }

    public static<T> PageData<T> fromPageInfo(PageInfo<T> pageInfo) {
        return new PageData<>(pageInfo.getTotal(), pageInfo.getList());
    }
}
