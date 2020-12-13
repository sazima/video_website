package com.video.tanmu.controller;

import com.video.tanmu.param.TanmuInsertParam;
import com.video.tanmu.param.TanmuQueryParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.TanmuService;
import com.video.tanmu.vo.VideoTanmuVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/tanmu")
public class TanmuController {
    @Autowired
    private TanmuService tanmuService;

    @RequestMapping("/getByVideo")
    @ResponseBody
    public Response<Map<Integer, List<VideoTanmuVo>>> selectByVideo(TanmuQueryParam tanmuQueryParam) {
        return tanmuService.selectByVideo(tanmuQueryParam);
    }

    @RequestMapping(value = "/insert", method = RequestMethod.POST)
    @ResponseBody
    public Response<Integer> insert(@RequestBody TanmuInsertParam tanmuInsertParam) {
        return tanmuService.insert(tanmuInsertParam);
    }


}
