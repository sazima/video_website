package com.video.tanmu.controller;

import com.video.tanmu.param.TanmuInsertParam;
import com.video.tanmu.param.TanmuInsertV3Param;
import com.video.tanmu.param.TanmuQueryParam;
import com.video.tanmu.param.TanmuQueryV3Param;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.TanmuService;
import com.video.tanmu.vo.VideoTanmuV3InsertResultVo;
import com.video.tanmu.vo.VideoTanmuVo;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@RestController
@RequestMapping("/tanmu")
public class TanmuController {

    Logger logger = LoggerFactory.getLogger(TanmuController.class);

    @Autowired
    private TanmuService tanmuService;


    @RequestMapping(value = "/v3", method = RequestMethod.GET)
    @ResponseBody
    public HashMap<Object, Object> tanmu(TanmuQueryV3Param tanmuQueryParam) {
        Response<ArrayList> res = tanmuService.selectByVideoV3(tanmuQueryParam);
        HashMap<Object, Object> map = new HashMap<>();
        map.put("code", 0);
        map.put("data", res.getData());
        return map;
    }
    @RequestMapping(value = "/v3", method = RequestMethod.POST)
    @ResponseBody
    public   Response<VideoTanmuV3InsertResultVo> tanmu( @RequestBody TanmuInsertV3Param insertV3Param) {
        return tanmuService.CreateByVideoV3(insertV3Param);
    }


    @RequestMapping("/getByVideo")
    @ResponseBody
    public Response<List<VideoTanmuVo>> selectByVideo(TanmuQueryParam tanmuQueryParam) {
        return tanmuService.selectByVideo(tanmuQueryParam);
    }

    @RequestMapping(value = "/insert", method = RequestMethod.POST)
    @ResponseBody
    public Response<Integer> insert(@RequestBody TanmuInsertParam tanmuInsertParam) {
        return tanmuService.insert(tanmuInsertParam);
    }
}
