package com.video.tanmu.service;

import com.video.tanmu.result.Response;
import com.video.tanmu.vo.TypeVo;

import java.util.List;

public interface TypeService {
    Response<List<TypeVo>> selectAll();
}
