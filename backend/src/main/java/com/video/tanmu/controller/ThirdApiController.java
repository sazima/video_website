package com.video.tanmu.controller;

import com.video.tanmu.constants.ResponseCode;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ThirdCollectionService;
import com.video.tanmu.vo.TaskInfoVo;
import com.video.tanmu.vo.ThirdCollectionApiVo;
import com.video.tanmu.vo.ThirdTypesResponseDataVo;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
@RequestMapping("/admin/collection")
public class ThirdApiController {
    private Logger logger = LoggerFactory.getLogger(ThirdApiController.class);
    @Value("${collection.url}")
    private String collectionUrl;

    @Autowired
    private ThirdCollectionService thirdCollectionService;
    @RequestMapping("/getAll")
    @ResponseBody
    public Response<List<ThirdCollectionApiVo>> selectAll( UserModel userModel){
        if (null == userModel) {
            return new Response(ResponseCode.NOT_LOGIN);
        }
        return thirdCollectionService.selectAll();
    }
    @RequestMapping("/updateOrCreate")
    @ResponseBody
    public Response<Integer> updateOrCreate(@RequestBody  ThirdCollectionApiVo thirdCollectionApiVo){
        return thirdCollectionService.updateOrCreate(thirdCollectionApiVo);
    }

    @RequestMapping("/startTask")
    public Response<String> startTask(@RequestParam("key") String key, @RequestParam("hour") String hour, UserModel userModel){
        if (null == userModel) {
            return new Response(ResponseCode.NOT_LOGIN);
        }
        RestTemplate restTemplate = new RestTemplate();
        String url = collectionUrl + "/api/collectionVideo/start_task?key=" + key + "&hour=" + hour;
        String result = restTemplate.getForObject(url, String.class);
        logger.info("url > " + url);
        return Response.success(result);
    }
    @RequestMapping("/getTaskByKey")
    public Response<TaskInfoVo> get_task_by_key(@RequestParam("key") String key){
        RestTemplate restTemplate = new RestTemplate();
        String url = collectionUrl + "/api/collectionVideo/get_task_by_key?key=" + key;
        TaskInfoVo taskInfoVo = restTemplate.getForObject(url, TaskInfoVo.class);
        logger.info("url > " + url);
        return Response.success(taskInfoVo);
    }

    @RequestMapping("/getTypesByKey")
    public Response<ThirdTypesResponseDataVo> getTypesByKey(@RequestParam("key") String key){
        RestTemplate restTemplate = new RestTemplate();
        String url = collectionUrl + "/api/collectionVideo/get_types_by_key?key=" + key;
        ThirdTypesResponseDataVo thirdTypesResponseDataVo = restTemplate.getForObject(url, ThirdTypesResponseDataVo.class);
        logger.info("url > " + url);
        return Response.success(thirdTypesResponseDataVo);
    }
}
