package com.video.tanmu.service.impl;

import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.dao.VideoLinkDao;
import com.video.tanmu.dao.VideoTanmuDao;
import com.video.tanmu.model.VideoLinkModel;
import com.video.tanmu.model.VideoModel;
import com.video.tanmu.model.VideoTanmuModel;
import com.video.tanmu.param.TanmuInsertParam;
import com.video.tanmu.param.TanmuQueryParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.TanmuService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.vo.VideoTanmuVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class TanmuServiceImpl implements TanmuService {
    @Autowired
    private VideoTanmuDao videoTanmuDao;

    @Autowired
    private VideoLinkDao videoLinkDao;

    @Autowired
    private VideoDao videoDao;

    @Override
    public Response<Map<Integer, List<VideoTanmuVo>>> selectByVideo(TanmuQueryParam queryParam) {
        if (null == queryParam.getAv()) {
            return Response.fail("指定视频av");
        }
        if (StringUtils.isBlank(queryParam.getFromName())) {
            return Response.fail("需要指定来源");
        }
        if (StringUtils.isBlank(queryParam.getPlayName())) {
            return Response.fail("需要指定来源");
        }
        VideoModel videoModel = videoDao.selectByAv(queryParam.getAv());
        if (null == videoModel) {
            return Response.fail("视频不存在");
        }
        Map<Integer, List<VideoTanmuVo>> tanmuMap = new HashMap<>();
        tanmuMap.put(1, Collections.singletonList(new VideoTanmuVo("发送一条弹幕试试吧!!", 1.5, 1)));
        tanmuMap.put(2, Collections.singletonList(new VideoTanmuVo("弹幕有你更精彩", 2.5, 2)));
        List<VideoTanmuModel> videoTanmusModels = videoTanmuDao.selectByVideo(videoModel.getId(), queryParam.getFromName(), queryParam.getPlayName());
        for (VideoTanmuModel tanmu : videoTanmusModels) {
            VideoTanmuVo tanmuVo = ConvertUtils.copyProperties(tanmu, VideoTanmuVo.class);
            if (tanmuMap.containsKey(tanmu.getCurrentTimeInt())) {
                tanmuMap.get(tanmu.getCurrentTimeInt()).add(tanmuVo);
            } else {
                tanmuMap.put(tanmu.getCurrentTimeInt(), Collections.singletonList(tanmuVo));
            }
        }
        return Response.success(tanmuMap);
    }

    @Override
    public Response<Integer> insert(TanmuInsertParam tanmuInsertParam) {
        if (StringUtils.isBlank(tanmuInsertParam.getAv())) {
            return Response.fail("视频不存在");
        }
        if (StringUtils.isBlank(tanmuInsertParam.getContent())) {
            return Response.fail("请输入弹幕内容");
        }
        if (tanmuInsertParam.getCurrentTime() <= 0) {
            return Response.fail("视频开始播放后才可以发送弹幕");
        }
        if (StringUtils.isBlank(tanmuInsertParam.getFromName()) ||
                StringUtils.isBlank(tanmuInsertParam.getPlayName())) {
            return Response.fail("请指定视频");
        }
        VideoModel videoModel = videoDao.selectByAv(tanmuInsertParam.getAv());
        if (null == videoModel) {
            return Response.fail("视频不存在");
        }
        VideoLinkModel videoLinkModel = videoLinkDao.selectByFromAndName(tanmuInsertParam.getFromName(), tanmuInsertParam.getPlayName(), videoModel.getId());
        if (null == videoLinkModel) {
            return Response.fail("没有该视频选集");
        }
        VideoTanmuModel videoTanmuModel = new VideoTanmuModel();
        videoTanmuModel.setVideoId(videoModel.getId());
        videoTanmuModel.setContent(tanmuInsertParam.getContent());
        videoTanmuModel.setFromName(tanmuInsertParam.getFromName());
        videoTanmuModel.setPlayName(tanmuInsertParam.getPlayName());
        videoTanmuModel.setPlayUrl(videoLinkModel.getPlayUrl());
        videoTanmuModel.setVideoLinkId(videoLinkModel.getId());
        videoTanmuModel.setCurrentTime(tanmuInsertParam.getCurrentTime());
        videoTanmuModel.setCurrentTimeInt(tanmuInsertParam.getCurrentTime().intValue());
        int inserted = videoTanmuDao.insertSelective(videoTanmuModel);
        return Response.success(inserted);
    }
}
