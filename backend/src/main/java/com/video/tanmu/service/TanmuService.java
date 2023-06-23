package com.video.tanmu.service;

import com.video.tanmu.param.TanmuInsertParam;
import com.video.tanmu.param.TanmuInsertV3Param;
import com.video.tanmu.param.TanmuQueryParam;
import com.video.tanmu.param.TanmuQueryV3Param;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.VideoTanmuV3InsertResultVo;
import com.video.tanmu.vo.VideoTanmuVo;

import java.util.ArrayList;
import java.util.List;

public interface TanmuService {
    Response<List<VideoTanmuVo>> selectByVideo(TanmuQueryParam queryParam);

    Response<ArrayList> selectByVideoV3(TanmuQueryV3Param queryParam);

    Response<VideoTanmuV3InsertResultVo> CreateByVideoV3(TanmuInsertV3Param insertV3Param);

    Response<Integer> insert(TanmuInsertParam tanmuInsertParam);
}
