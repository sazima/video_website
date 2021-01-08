package com.video.tanmu.redis;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;

import java.time.Duration;
import java.util.List;
import java.util.concurrent.TimeUnit;

@Component
public class RedisClient {

    @Autowired
    private StringRedisTemplate redisTemplate;

    @Value("${spring.redis.prefix}")
    private String prefix;

    @Value("${spring.redis.expired-seconds}")
    private Integer defaultExpiredSecond;


    public <T> T get(String key, Class<T> clazz) {
        String str = redisTemplate.opsForValue().get(prefix + key);
        return stringToBean(str, clazz);
    }


    public <T> List<T> getList(String key, Class<T> clazz) {
        String str = redisTemplate.opsForValue().get(prefix + key);
        return JSONObject.parseArray(str, clazz);
    }

    public <T> void set(String key, T value) {
        set(key, value, defaultExpiredSecond);
    }

    public void set(String key, Object value, int timeout) {
        String s = beanToString(value);
        redisTemplate.opsForValue().set(prefix + key, s, timeout, TimeUnit.SECONDS);
    }

    public Long incr(String key) {
        return redisTemplate.opsForValue().increment(prefix + key);
    }

    public void  expire(String key, Integer seconds) {
        redisTemplate.expire(prefix + key, Duration.ofSeconds(seconds));
    }

    public void expire(String key, int timeout) {
        redisTemplate.expire(prefix + key, timeout, TimeUnit.SECONDS);
    }

    private static <T> String beanToString(T value) {
        if(value == null) {
            return null;
        }
        Class<?> clazz = value.getClass();
        if(clazz == int.class || clazz == Integer.class) {
            return ""+value;
        }else if(clazz == String.class) {
            return (String)value;
        }else if(clazz == long.class || clazz == Long.class) {
            return ""+value;
        }else {
            return JSON.toJSONString(value);
        }
    }

    @SuppressWarnings("unchecked")
    private static <T> T stringToBean(String str, Class<T> clazz) {
        if (str == null || clazz == null) {
            return null;
        }
        if (clazz == String.class) {
            return (T) str;
        }
        if(clazz == int.class || clazz == Integer.class) {
            return (T)Integer.valueOf(str);
        } else if(clazz == long.class || clazz == Long.class) {
            return  (T)Long.valueOf(str);
        }  else{
            return JSON.toJavaObject(JSON.parseObject(str), clazz);
        }
    }
}
