package com.video.tanmu.service.impl;

import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.dao.VideoLinkDao;
import com.video.tanmu.model.VideoLinkModel;
import com.video.tanmu.model.VideoModel;
import com.video.tanmu.param.PageParam;
import com.video.tanmu.param.VideoQueryParam;
import com.video.tanmu.result.PageData;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.VideoService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.utils.RedisClient;
import com.video.tanmu.vo.VideoDetailVo;
import com.video.tanmu.vo.VideoListVo;
import com.video.tanmu.vo.VideoPlayGroup;
import com.video.tanmu.vo.VideoPlayUrlVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class VideoServiceImpl implements VideoService {
    @Autowired
    private VideoDao videoDao;

    @Autowired
    private VideoLinkDao videoLinkDao;

    @Autowired
    private RedisClient redisClient ;

    @Override
    public Response<PageData<VideoListVo>> pageByQuery(VideoQueryParam videoQueryParam, PageParam pageParam) {
        String totalKey = "kw::" + videoQueryParam.getKw() + "typeId::" + videoQueryParam.getTypeId();
        Integer total = redisClient.get(totalKey, Integer.class);
        // total缓存
        if (null == total) {
            total = videoDao.selectTotalByQuery(videoQueryParam);
            redisClient.set(totalKey, total);
        }
        List<VideoModel> videoModels = videoDao.selectByQuery(videoQueryParam, pageParam.getOffset(), pageParam.getPageSize());
        List<VideoListVo> videoListVos = videoModels.stream().map(VideoListVo::convertFromVideoModel).collect(Collectors.toList());
        PageData<VideoListVo> videoPageData = new PageData<>(total, videoListVos);
        return Response.success(videoPageData);
    }

    @Override
    public Response<VideoDetailVo> getDetailByAv(String av) {
        String key = "videoByAv::" + av;
        if (StringUtils.isBlank(av)) {
            return Response.fail("请指定av号");
        }
        VideoModel videoModel = videoDao.selectByAv(av);
        if (null == videoModel) {
            return Response.fail("视频不存在");
        }
        VideoDetailVo videoDetailVoCache = redisClient.get(key, VideoDetailVo.class);
        if (null != videoDetailVoCache) {
            return Response.success(videoDetailVoCache);
        }
        List<VideoLinkModel> videoLinkModels = videoLinkDao.selectByVideoId(videoModel.getId());
        VideoDetailVo videoDetailVo = ConvertUtils.copyProperties(videoModel, VideoDetailVo.class);
        List<VideoPlayGroup> videoPlayGroupList = linksToPlayGroup(videoLinkModels);
        videoDetailVo.setVideoPlayGroupList(videoPlayGroupList);
        redisClient.set(key, videoDetailVo);
        return Response.success(videoDetailVo);
    }

    /**
     * 对播放链接进行分组
     */
    private List<VideoPlayGroup> linksToPlayGroup(List<VideoLinkModel> videoLinkModels) {
        List<VideoPlayGroup> videoPlayGroupList = new ArrayList<>();

        HashMap<String, VideoPlayGroup> stringVideoPlayGroupHashMap = new HashMap<>();

        for (VideoLinkModel videoLinkModel : videoLinkModels) {
            if (stringVideoPlayGroupHashMap.containsKey(videoLinkModel.getFromName())) {
                VideoPlayGroup videoPlayGroup = stringVideoPlayGroupHashMap.get(videoLinkModel.getFromName());
                VideoPlayUrlVo videoPlayUrlVo = new VideoPlayUrlVo(videoLinkModel.getPlayName(), videoLinkModel.getPlayUrl());
            } else {
                VideoPlayGroup videoPlayGroup = new VideoPlayGroup();
                videoPlayGroup.setFromName(videoLinkModel.getFromName());

                stringVideoPlayGroupHashMap.put(videoLinkModel.getFromName(), videoPlayGroup);

                VideoPlayUrlVo videoPlayUrlVo = new VideoPlayUrlVo(videoLinkModel.getPlayName(), videoLinkModel.getPlayUrl());
                videoPlayGroup.setVideoPlayUrlVoList(Collections.singletonList(videoPlayUrlVo));
                videoPlayGroupList.add(videoPlayGroup);
            }
        }
        return videoPlayGroupList;
    }

}
