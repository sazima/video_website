package com.video.tanmu.controller;

import com.video.tanmu.param.PageParam;
import com.video.tanmu.param.VideoQueryParam;
import com.video.tanmu.result.PageData;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.VideoService;
import com.video.tanmu.vo.VideoDetailVo;
import com.video.tanmu.vo.VideoListVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/video")
public class VideoController {
    @Autowired
    private VideoService videoService;

    @RequestMapping("/pageByQuery")
    @ResponseBody
    public Response<PageData<VideoListVo>> pageByQuery(VideoQueryParam videoQueryParam, PageParam pageParam) {
        if (StringUtils.isBlank(videoQueryParam.getKw())) {
            videoQueryParam.setKw(null);
        }
        return videoService.pageByQuery(videoQueryParam, pageParam);
    }

    @RequestMapping("/detail")
    @ResponseBody
    public Response<VideoDetailVo> getDetailByAv(@RequestParam("av") String av) {
        return videoService.getDetailByAv(av);
    }
}
