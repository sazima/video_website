package com.video.tanmu.service.impl;

import com.video.tanmu.dao.ConfigDao;
import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.dao.VideoLinkDao;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.model.VideoLinkModel;
import com.video.tanmu.model.VideoModel;
import com.video.tanmu.param.PageParam;
import com.video.tanmu.param.VideoQueryParam;
import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.redis.VideoKey;
import com.video.tanmu.result.PageData;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ConfigService;
import com.video.tanmu.service.VideoService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.utils.RequestUtils;
import com.video.tanmu.vo.VideoDetailVo;
import com.video.tanmu.vo.VideoListVo;
import com.video.tanmu.vo.VideoPlayGroup;
import com.video.tanmu.vo.VideoPlayUrlVo;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class VideoServiceImpl implements VideoService {
    Logger logger = LoggerFactory.getLogger(VideoService.class);


    @Autowired
    private VideoDao videoDao;

    @Autowired
    private VideoLinkDao videoLinkDao;

    @Autowired
    private ConfigService configService;

    @Autowired
    private RedisClient redisClient;

    @Override
    public Response<PageData<VideoListVo>> pageByQuery(VideoQueryParam videoQueryParam, PageParam pageParam, UserModel userModel) {
        logger.info("{} query video list, type {}, kw {}", RequestUtils.getRemoteIp(), videoQueryParam.getTypeId(), videoQueryParam.getKw());
        List<Integer> noLoginTypeId = configService.getNoLoginTypeId();
        if (null == userModel && noLoginTypeId.contains(videoQueryParam.getTypeId())) {
            return Response.success(new PageData<>());
        }
        String totalKey = VideoKey.getTotalByQueryParam(videoQueryParam);
        Integer total = redisClient.get(totalKey, Integer.class);
        // total缓存
        if (null == total) {
            total = videoDao.selectTotalByQuery(videoQueryParam);
            redisClient.set(totalKey, total);
        }
        List<VideoModel> videoModels = null;
        if (null == userModel && videoQueryParam.getTypeId() == null) {
            videoModels = videoDao.selectByQuery(videoQueryParam, pageParam.getOffset(), pageParam.getPageSize(), noLoginTypeId);
        } else {
            videoModels = videoDao.selectByQuery(videoQueryParam, pageParam.getOffset(), pageParam.getPageSize(), null);
        }
        List<VideoListVo> videoListVos = videoModels.stream().map(VideoListVo::convertFromVideoModel).collect(Collectors.toList());
        PageData<VideoListVo> videoPageData = new PageData<>(total, videoListVos);
        return Response.success(videoPageData);
    }

    @Override
    public Response<VideoDetailVo> getDetailByAv(String av) {
        String key = VideoKey.getVideoByAvKey(av);
        if (StringUtils.isBlank(av)) {
            return Response.fail("请指定av号");
        }
        VideoDetailVo videoDetailVoCache = redisClient.get(key, VideoDetailVo.class);
        if (null != videoDetailVoCache) {
            logger.info("{}, 获取视频: {}", RequestUtils.getRemoteIp(), videoDetailVoCache.getName());
            return Response.success(videoDetailVoCache);
        }
        VideoModel videoModel = videoDao.selectByAv(av);
        if (null == videoModel) {
            return Response.fail("视频不存在");
        }
        List<VideoLinkModel> videoLinkModels = videoLinkDao.selectByVideoId(videoModel.getId());
        VideoDetailVo videoDetailVo = ConvertUtils.copyProperties(videoModel, VideoDetailVo.class);
        List<VideoPlayGroup> videoPlayGroupList = linksToPlayGroup(videoLinkModels);
        videoDetailVo.setVideoPlayGroupList(videoPlayGroupList);
        redisClient.set(key, videoDetailVo);
        logger.info("{}, 获取视频: {}", RequestUtils.getRemoteIp(), videoModel.getName());
        return Response.success(videoDetailVo);
    }

    /**
     * 对播放链接进行分组
     */
    private List<VideoPlayGroup> linksToPlayGroup(List<VideoLinkModel> videoLinkModels) {
        List<VideoPlayGroup> videoPlayGroupList = new ArrayList<>();

        HashMap<String, VideoPlayGroup> stringVideoPlayGroupHashMap = new HashMap<>();

        List<String> proxyPrefixList = configService.getProxyPrefixList();

        for (VideoLinkModel videoLinkModel : videoLinkModels) {

            ArrayList<VideoPlayUrlVo.Url> urls = new ArrayList<>();
            urls.add(new VideoPlayUrlVo.Url(videoLinkModel.getPlayUrl(), "原版线路", false));
            for (int i = 0 ; i< proxyPrefixList.size(); i++) {
                urls.add(new VideoPlayUrlVo.Url(proxyPrefixList.get(i) + videoLinkModel.getPlayUrl(), "线路" + i, false));
            }
            urls.get(0).setSelected(true);
            VideoPlayUrlVo videoPlayUrlVo = new VideoPlayUrlVo(videoLinkModel.getPlayName(), urls);


            if (stringVideoPlayGroupHashMap.containsKey(videoLinkModel.getFromName())) {
                VideoPlayGroup videoPlayGroup = stringVideoPlayGroupHashMap.get(videoLinkModel.getFromName());
                videoPlayGroup.getVideoPlayUrlVoList().add(videoPlayUrlVo);
            } else {
                VideoPlayGroup videoPlayGroup = new VideoPlayGroup();
                videoPlayGroup.setFromName(videoLinkModel.getFromName());
                stringVideoPlayGroupHashMap.put(videoLinkModel.getFromName(), videoPlayGroup);
                videoPlayGroup.setVideoPlayUrlVoList(new ArrayList<>(Collections.singletonList(videoPlayUrlVo)));
                videoPlayGroupList.add(videoPlayGroup);
            }
        }
        // 排序，集数多的放前面
        videoPlayGroupList.sort(new VideoPlayGroupComparator());
        return videoPlayGroupList;
    }
    private static class VideoPlayGroupComparator implements Comparator<VideoPlayGroup>
    {
        public int compare(VideoPlayGroup a, VideoPlayGroup b)
        {
            return b.getVideoPlayUrlVoList().size() - a.getVideoPlayUrlVoList().size() ;
        }

    }


}

