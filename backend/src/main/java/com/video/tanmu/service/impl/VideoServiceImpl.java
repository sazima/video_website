package com.video.tanmu.service.impl;

import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.dao.VideoLinkDao;
import com.video.tanmu.model.Video;
import com.video.tanmu.model.VideoLink;
import com.video.tanmu.param.PageParam;
import com.video.tanmu.param.VideoQueryParam;
import com.video.tanmu.result.PageData;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.VideoService;
import com.video.tanmu.utils.ConvertUtils;
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

@Service
public class VideoServiceImpl implements VideoService {
    @Autowired
    private VideoDao videoDao;

    @Autowired
    private VideoLinkDao videoLinkDao;

    @Override
    public Response<PageData<VideoListVo>> pageByQuery(VideoQueryParam videoQueryParam, PageParam pageParam) {
        PageHelper.startPage(pageParam.getPage(), pageParam.getPageSize());
        List<Video> videos = videoDao.selectByQuery(videoQueryParam);
        long total = ((Page) videos).getTotal();
        List<VideoListVo> videoListVos = ConvertUtils.copyListProperties(videos, VideoListVo.class);
        PageData<VideoListVo> videoPageData = new PageData<>(total, videoListVos);
        return Response.success(videoPageData);
    }

    @Override
    public Response<VideoDetailVo> getDetailByAv(String av) {
        if (StringUtils.isBlank(av)) {
            return Response.fail("请指定av号");
        }
        Video video = videoDao.selectByAv(av);
        if (null == video) {
            return Response.fail("视频不存在");
        }
        List<VideoLink> videoLinks = videoLinkDao.selectByVideoId(video.getId());

        VideoDetailVo videoDetailVo = ConvertUtils.copyProperties(video, VideoDetailVo.class);
        List<VideoPlayGroup> videoPlayGroupList = linksToPlayGroup(videoLinks);
        videoDetailVo.setVideoPlayGroupList(videoPlayGroupList);
        return Response.success(videoDetailVo);
    }

    /**
     * 对播放链接进行分组
     */
    private List<VideoPlayGroup> linksToPlayGroup(List<VideoLink> videoLinks) {
        List<VideoPlayGroup> videoPlayGroupList = new ArrayList<>();

        HashMap<String, VideoPlayGroup> stringVideoPlayGroupHashMap = new HashMap<>();

        for (VideoLink videoLink : videoLinks) {
            if (stringVideoPlayGroupHashMap.containsKey(videoLink.getFromName())) {
                VideoPlayGroup videoPlayGroup = stringVideoPlayGroupHashMap.get(videoLink.getFromName());
                VideoPlayUrlVo videoPlayUrlVo = new VideoPlayUrlVo(videoLink.getPlayName(), videoLink.getPlayUrl());
                videoPlayGroup.getVideoPlayUrlVoList().add(videoPlayUrlVo);
            } else {
                VideoPlayGroup videoPlayGroup = new VideoPlayGroup();
                videoPlayGroup.setFromName(videoLink.getFromName());
                stringVideoPlayGroupHashMap.put(videoLink.getFromName(), videoPlayGroup);
                VideoPlayUrlVo videoPlayUrlVo = new VideoPlayUrlVo(videoLink.getPlayName(), videoLink.getPlayUrl());
                videoPlayGroup.setVideoPlayUrlVoList(Collections.singletonList(videoPlayUrlVo));
                videoPlayGroupList.add(videoPlayGroup);
            }
        }
        return videoPlayGroupList;
    }

}
