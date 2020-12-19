package com.video.tanmu.redis;

public class UserKey {

    public static String getTokenKey(String token) {
        return "tokenUserId::" + token;
    }

    public static String getTokenListKey(Integer userId) {
        return "userIdToken::" + userId;
    }

    public static String getUserByUserIdKey(Integer userId) {
        return "userModelById::" + userId;
    }
}
