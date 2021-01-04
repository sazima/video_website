package com.video.tanmu.controller;

import com.video.tanmu.model.UserModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.IndexService;
import com.video.tanmu.vo.IndexTreeVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/index")
public class IndexController {
    @Autowired
    private IndexService indexService;

    @RequestMapping("/indexTree")
    @ResponseBody
    public Response<IndexTreeVo> getIndexTree(UserModel userModel) {
        return indexService.getIndexTree(userModel);
    }
}
