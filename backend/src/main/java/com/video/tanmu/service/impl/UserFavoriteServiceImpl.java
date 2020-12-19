package com.video.tanmu.service.impl;

import com.video.tanmu.dao.UserDao;
import com.video.tanmu.dao.UserFavoriteDao;
import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.model.UserFavoriteModel;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.model.VideoModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.UserFavoriteService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.vo.VideoListVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


@Service
public class UserFavoriteServiceImpl implements UserFavoriteService {
    @Autowired
    private VideoDao videoDao;
    @Autowired
    private UserDao userDao;
    @Autowired
    private UserFavoriteDao userFavoriteDao;

    @Override
    public Response<Integer> addFavoriteVideo(Integer userId, String av) {
        VideoModel videoModel = videoDao.selectByAv(av);
        if (null == videoModel) {
            return Response.fail("该视频不存在");
        }
        UserModel userModel = userDao.selectByPrimaryKey(userId);
        if (null == userModel) {
            return Response.fail("用户状态异常");
        }
        UserFavoriteModel userFavoriteModel = new UserFavoriteModel();
        userFavoriteModel.setUserId(userId);
        userFavoriteModel.setAv(av);
        userFavoriteModel.setAddTime(Instant.now().getEpochSecond());
        int i = userFavoriteDao.insertSelective(userFavoriteModel);
        return Response.success(i);
    }

    @Override
    public Response<List<VideoListVo>> getFavoriteVideoListByUserId(Integer userId) {
        List<String> avList = userFavoriteDao.selectAvListByUserId(userId);
        if (CollectionUtils.isEmpty(avList)) {
            return Response.success(new ArrayList<>());
        }
        List<VideoModel> videoModels = videoDao.selectByAvList(avList);
        List<VideoListVo> videoListVos = ConvertUtils.copyListProperties(videoModels, VideoListVo.class);
        return Response.success(videoListVos);
    }


    @Override
    public Response<Integer> removeFavoriteVideo(Integer userId, String av){
        int i = userFavoriteDao.removeByUserIdAndAv(userId, av);
        return Response.success(i);
    }

}
