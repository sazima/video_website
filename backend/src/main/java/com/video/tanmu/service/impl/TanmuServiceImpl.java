package com.video.tanmu.service.impl;

import com.alibaba.fastjson.JSON;
import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.dao.VideoLinkDao;
import com.video.tanmu.dao.VideoTanmuDao;
import com.video.tanmu.model.VideoLinkModel;
import com.video.tanmu.model.VideoModel;
import com.video.tanmu.model.VideoTanmuModel;
import com.video.tanmu.param.TanmuInsertParam;
import com.video.tanmu.param.TanmuInsertV3Param;
import com.video.tanmu.param.TanmuQueryParam;
import com.video.tanmu.param.TanmuQueryV3Param;
import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ConfigService;
import com.video.tanmu.service.TanmuService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.utils.RequestUtils;
import com.video.tanmu.vo.VideoTanmuV3InsertResultVo;
import com.video.tanmu.vo.VideoTanmuVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.Serializable;
import java.util.*;

@Service
public class TanmuServiceImpl implements TanmuService {
    @Autowired
    private VideoTanmuDao videoTanmuDao;

    @Autowired
    private VideoLinkDao videoLinkDao;

    @Autowired
    private VideoDao videoDao;

    @Autowired
    private ConfigService configService;
    @Autowired
    private RedisClient redisClient;

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
        // 随机弹幕
        List<String> messageList = new ArrayList<>(configService.getRandomTanmuList());
        for (int i = 5; i <= 30; i += 2) {
            if (messageList.size() == 0) {
                break;
            }
            tanmuMap.put(i, new ArrayList<>(Collections.singletonList(new VideoTanmuVo(messageList.remove(new Random().nextInt(messageList.size())), 0.5 + i, i))));
        }
        // 视频弹幕
        List<VideoTanmuModel> videoTanmusModels = videoTanmuDao.selectByVideo(videoModel.getId(), queryParam.getFromName(), queryParam.getPlayName());
        for (VideoTanmuModel tanmu : videoTanmusModels) {
            VideoTanmuVo tanmuVo = ConvertUtils.copyProperties(tanmu, VideoTanmuVo.class);
            if (tanmuMap.containsKey(tanmu.getCurrentTimeInt())) {
                tanmuMap.get(tanmu.getCurrentTimeInt()).add(tanmuVo);
            } else {
                tanmuMap.put(tanmu.getCurrentTimeInt(), new ArrayList<>(Collections.singletonList(tanmuVo)));
            }
        }
        return Response.success(tanmuMap);
    }
    @Override
    public Response<ArrayList> selectByVideoV3(TanmuQueryV3Param queryParam) {
        String[] split = queryParam.getId().split("~");
        String av = split[0];
        String fromName = split[1];
        String playName = split[2];
        VideoModel videoModel = videoDao.selectByAv(av);
        if (null == videoModel) {
            return Response.fail("视频不存在");
        }
//        // 视频弹幕
        List<VideoTanmuModel> videoTanmusModels = videoTanmuDao.selectByVideo(videoModel.getId(), fromName, playName);
        ArrayList voList = new ArrayList<>();
        for (VideoTanmuModel model : videoTanmusModels) {
            String style = model.getStyle();
            Integer color = 16777215;
            Integer type = 0;
            if (!StringUtils.isEmpty(style)) {
                Map<String, String> parse = (Map<String, String>) JSON.parse(style);
                color = Integer.valueOf(parse.get("color"));
                type = Integer.valueOf(parse.get("type"));
            }
            List<? extends Serializable> l = Arrays.asList(model.getCurrentTime(), type, color, "test11111", model.getContent());
            voList.add(l);
        }
        Response<ArrayList> success = Response.success(voList);
        success.setCode(0);
        return success;
    }


    @Override
    public Response<VideoTanmuV3InsertResultVo> CreateByVideoV3(TanmuInsertV3Param insertV3Param) {
        String[] split = insertV3Param.getId().split("~");
        String av = split[0];
        String fromName = split[1];
        String playName = split[2];
        String text = insertV3Param.getText();
        if (StringUtils.isBlank(text)) {
            return Response.fail("内容不能为空");
        }
        VideoModel videoModel = videoDao.selectByAv(av);
        if (null == videoModel) {
            return Response.fail("视频不存在");
        }
        VideoLinkModel videoLinkModel = videoLinkDao.selectByFromAndName(fromName, playName, videoModel.getId());
        if (null == videoLinkModel) {
            return Response.fail("没有该视频选集");
        }
        if (!RequestUtils.checkFrequency(1, 10)) {
            return Response.fail("你太快了");
        }
        VideoTanmuModel model = new VideoTanmuModel();
        model.setVideoId(videoModel.getId());
        model.setContent(text);
        model.setFromName(fromName);
        model.setPlayName(playName);
        model.setPlayUrl(videoLinkModel.getPlayUrl());
        model.setVideoLinkId(videoLinkModel.getId());
        model.setCurrentTime(insertV3Param.getTime());
        model.setCurrentTimeInt(insertV3Param.getTime().intValue());
        HashMap<Object, Object> style = new HashMap<>();
        style.put("type", insertV3Param.getType());
        style.put("color", insertV3Param.getColor());
        model.setStyle(JSON.toJSONString(style));
        int inserted = videoTanmuDao.insertSelective(model);
        VideoTanmuV3InsertResultVo insertResult = new VideoTanmuV3InsertResultVo();
        insertResult.setTime(model.getCurrentTime());
        insertResult.setPlayer(insertV3Param.getId());
        insertResult.setAuthor("");
        insertResult.setText(model.getContent());
        insertResult.setColor(insertV3Param.getColor());
        insertResult.setType(insertV3Param.getType());
        Response<VideoTanmuV3InsertResultVo> success = Response.success(insertResult);
        success.setCode(0);
        return success;
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
        if (!RequestUtils.checkFrequency(1, 10)) {
            return Response.fail("你太快了");
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
