package com.video.tanmu.controller;

import com.video.tanmu.model.UserModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.IndexService;
import com.video.tanmu.utils.RequestUtils;
import com.video.tanmu.vo.IndexTreeVo;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/index")
public class IndexController {
    Logger logger = LoggerFactory.getLogger(IndexController.class);

    @Autowired
    private IndexService indexService;

    @RequestMapping("/indexTree")
    @ResponseBody
    public Response<IndexTreeVo> getIndexTree(UserModel userModel) {
        logger.info("ip: " + RequestUtils.getRemoteIp() + " get Index tree");
        return indexService.getIndexTree(userModel);
    }
}
