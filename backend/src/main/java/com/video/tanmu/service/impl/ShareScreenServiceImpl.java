package com.video.tanmu.service.impl;

import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.redis.WebSocketUidKey;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ShareScreenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class ShareScreenServiceImpl implements ShareScreenService {
    @Autowired
    private RedisClient redisClient;

    @Override
    public Response<String> generateUid() {
//        if (!RequestUtils.checkFrequency(2, 10)) {
//            return Response.fail("你太快了");
//        }
        String uid = UUID.randomUUID().toString();
        String key = WebSocketUidKey.getKeyByUid(uid);
        redisClient.set(key, 1);
        return Response.success(uid);
    }

    @Override
    public Response<Boolean> checkUid(String uid) {
        String key = WebSocketUidKey.getKeyByUid(uid);
        Integer integer = redisClient.get(key, Integer.class);
        return Response.success(integer != null);
    }

}
