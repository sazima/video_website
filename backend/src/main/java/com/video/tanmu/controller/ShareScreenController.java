package com.video.tanmu.controller;

import com.alibaba.fastjson.JSON;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ShareScreenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;


@RestController
@RequestMapping("/share")
public class ShareScreenController {

    @Autowired
    private ShareScreenService shareScreenService;

    @RequestMapping("/generateUid")
    @ResponseBody
    public Response<String> generateUid() {
        return shareScreenService.generateUid();
    }

    @RequestMapping("/checkUid")
    @ResponseBody
    public Response<Boolean> checkUid(@RequestParam("uid") String uid) {
        return shareScreenService.checkUid(uid);
    }

    @RequestMapping("/pushVideo")
    @ResponseBody
    public Response<String> pushVideoToUid() {
        HashMap<String, String> stringStringHashMap = new HashMap<>();
        stringStringHashMap.put("url", "https://video3.wktadmin.com/video_proxy/?url=https://youku.hao-yongjiu.com/20210216/7286_251ede43/index.m3u8");
        String s = "{\n" +
                "    \"url\":[\n" +
                "        {\n" +
                "            \"src\":\"https://youku.hao-yongjiu.com/20210216/7286_251ede43/index.m3u8\",\n" +
                "            \"type\":\"application/x-mpegURL\",\n" +
                "            \"label\":\"原版线路\",\n" +
                "            \"selected\":false\n" +
                "        },\n" +
                "        {\n" +
                "            \"src\":\"https://video1.wktadmin.com/video_proxy/?url=https://youku.hao-yongjiu.com/20210216/7286_251ede43/index.m3u8\",\n" +
                "            \"type\":\"application/x-mpegURL\",\n" +
                "            \"label\":\"线路0\",\n" +
                "            \"selected\":false\n" +
                "        },\n" +
                "        {\n" +
                "            \"src\":\"https://video2.wktadmin.com/video_proxy/?url=https://youku.hao-yongjiu.com/20210216/7286_251ede43/index.m3u8\",\n" +
                "            \"type\":\"application/x-mpegURL\",\n" +
                "            \"label\":\"线路1\",\n" +
                "            \"selected\":false\n" +
                "        },\n" +
                "        {\n" +
                "            \"src\":\"https://video3.wktadmin.com/video_proxy/?url=https://youku.hao-yongjiu.com/20210216/7286_251ede43/index.m3u8\",\n" +
                "            \"type\":\"application/x-mpegURL\",\n" +
                "            \"label\":\"线路2\",\n" +
                "            \"selected\":true\n" +
                "        }\n" +
                "    ],\n" +
                "    \"name\":\"HD高清\"\n" +
                "}";
        stringStringHashMap.put("name", "https://video3.wktadmin.com/video_proxy/?url=https://youku.hao-yongjiu.com/20210216/7286_251ede43/index.m3u8");
//        WebSocketController.sendToUid(uid, JSON.toJSONString(stringStringHashMap));
        WebSocketController.sendToAll(s);
        return null;
    }
}
