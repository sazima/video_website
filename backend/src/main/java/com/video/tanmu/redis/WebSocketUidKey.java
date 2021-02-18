package com.video.tanmu.redis;

public class WebSocketUidKey {
    public static String getKeyByUid(String uid) {
            return "websocket::uid::" + uid;
    }
}
