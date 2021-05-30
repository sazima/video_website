package com.video.tanmu.service;

import com.video.tanmu.param.TanmuInsertParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.ThirdCollectionApiVo;

import java.util.List;

public interface ThirdCollectionService {
    Response<List<ThirdCollectionApiVo>> selectAll();

    Response<Integer> updateOrCreate(ThirdCollectionApiVo thirdCollectionApiVo);
}
