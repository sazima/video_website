package com.video.tanmu.redis;

public class ConfigKey {
    public static String getRedisKeyByName(String name) {
        return "configname::" + name;
    }
}
