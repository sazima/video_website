package com.video.tanmu.config;

import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.result.RequestLimitException;
import com.video.tanmu.utils.RequestUtils;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.servlet.http.HttpServletRequest;

@Aspect
@Component
public class RequestLimitContract {

    private static final Logger logger = LoggerFactory.getLogger("RequestLimitLogger");
    @Autowired
    private RedisClient redisClient;

    @Before("@annotation(limit)")
    public void requestLimit(RequestLimit limit) throws RequestLimitException {
        try {
            HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.getRequestAttributes()).getRequest();
            String ip = RequestUtils.getRemoteIp();
            String url = request.getRequestURL().toString();
            String key = "req_limit_".concat(url).concat(ip);
            if (!RequestUtils.checkFrequency(key, limit.count(), limit.time())) {
                throw new RequestLimitException();
            }
        } catch (RequestLimitException e) {
            throw e;
        } catch (Exception e) {
            logger.error("发生异常: ", e);
        }
    }
}