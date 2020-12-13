package com.video.tanmu.service;

import com.video.tanmu.param.TanmuQueryParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.VideoTanmuVo;

import java.util.List;
import java.util.Map;

public interface TanmuService {
    Response<Map<Integer, List<VideoTanmuVo>>> selectByVideo(TanmuQueryParam queryParam);
}
