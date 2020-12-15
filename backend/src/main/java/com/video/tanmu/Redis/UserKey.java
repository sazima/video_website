package com.video.tanmu.Redis;

public class UserKey {

    public static String getTokenKey(String token) {
        return "tokenUserId::" + token;
    }

    public static String getTokenListKey(Integer userId) {
        return "userIdToken::" + userId;
    }
}
