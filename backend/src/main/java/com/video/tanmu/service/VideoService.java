package com.video.tanmu.service;

import com.video.tanmu.param.PageParam;
import com.video.tanmu.param.VideoQueryParam;
import com.video.tanmu.result.PageData;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.VideoDetailVo;
import com.video.tanmu.vo.VideoListVo;

public interface VideoService {

    Response<PageData<VideoListVo>> pageByQuery(VideoQueryParam videoQueryParam, PageParam pageParam);

    Response<VideoDetailVo> getDetailByAv(String av);
}
