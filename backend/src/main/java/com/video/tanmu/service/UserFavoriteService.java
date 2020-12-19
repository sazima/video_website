package com.video.tanmu.service;

import com.video.tanmu.result.Response;
import com.video.tanmu.vo.VideoListVo;

import java.util.List;

public interface UserFavoriteService {
    Response<Integer> addFavoriteVideo(Integer userId, String av);

    Response<List<VideoListVo>> getFavoriteVideoListByUserId(Integer userId);

    Response<Integer> removeFavoriteVideo(Integer userId, String av);
}
