package com.video.tanmu.utils;

import com.video.tanmu.config.SpringContext;
import com.video.tanmu.redis.RedisClient;
import org.apache.commons.lang3.StringUtils;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.servlet.http.HttpServletRequest;

public class RequestUtils {

    private static final String LOCALHOST_IPV4 = "127.0.0.1";
    private static final String LOCALHOST_IPV6 = "0:0:0:0:0:0:0:1";

    public static String getRemoteIp() {
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
        String remoteAddr = request.getRemoteAddr();
        if (StringUtils.isEmpty(remoteAddr) || remoteAddr.equals(RequestUtils.LOCALHOST_IPV6) || remoteAddr.equals(RequestUtils.LOCALHOST_IPV4)) {
            remoteAddr = request.getHeader("Cf-Connecting-Ip");
        }
        return remoteAddr;
    }

    public static boolean checkFrequency(Integer count, Integer limitTime) {
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
        String ip = RequestUtils.getRemoteIp();
        String url = request.getRequestURL().toString();
        String key = "req_limit_" + url + ip;
        return checkFrequency(key, count, limitTime);
    }
    public static boolean checkFrequency(String checkKey, Integer count, Integer limitTime) {
        RedisClient redisClient = SpringContext.getBean(RedisClient.class);
        Long incr = redisClient.incr(checkKey);
        if (incr == 1) {
            redisClient.expire(checkKey, limitTime);
        }
        return incr <= count;
    }
}
