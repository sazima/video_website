package com.video.tanmu.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import javax.websocket.*;
import javax.websocket.server.ServerEndpoint;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;


@ServerEndpoint("/ws")
@Component
public class WebSocketController {
    private static HashMap<String, Session> uidToSession = new HashMap<>();
    private static HashMap<Session, String> sessionToUid = new HashMap<>();
    /** 记录当前在线连接数 */
    private static AtomicInteger onlineCount = new AtomicInteger(0);
    static Logger log = LoggerFactory.getLogger(TanmuController.class);
    /**
     * 连接建立成功调用的方法
     */
    @OnOpen
    public void onOpen(Session session) throws IOException {
        onlineCount.incrementAndGet();
        List<String> uids = session.getRequestParameterMap().get("uid");
        if (uids.size() == 0) {
            session.close();
            return;
        } else {
            String uid = uids.get(0);
            uidToSession.put(uid, session);
            sessionToUid.put(session, uid);
        }
        log.info("有新连接加入：{}，当前在线人数为：{}", session.getId(), onlineCount.get());
    }

    @OnClose
    public void onClose(Session session) {
        onlineCount.decrementAndGet(); // 在线数减1
        String uid = sessionToUid.get(session);
        uidToSession.remove(uid);
        sessionToUid.remove(session);
        log.info("有一连接关闭：{}，当前在线人数为：{}", session.getId(), onlineCount.get());
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        log.info("服务端收到客户端[{}]的消息:{}", session.getId(), message);
        sendMessage("{}", session);
    }

    @OnError
    public void onError(Session session, Throwable error) {
        log.error("发生错误");
        error.printStackTrace();
    }

    /**
     * 服务端发送消息给客户端
     */
    private static void sendMessage(String message, Session toSession) {
        try {
            log.info("服务端给客户端[{}]发送消息{}", toSession.getId(), message);
            toSession.getBasicRemote().sendText(message);
        } catch (Exception e) {
            log.error("服务端发送消息给客户端失败：{}", e);
        }
    }

    public static boolean sendToUid(String message, String uid) {
        if (!uidToSession.containsKey(uid) ) {
            return false;
        }
        sendMessage(message, uidToSession.get(uid));
        return true;
    }
    public static boolean sendToAll(String message) {
        for (Session session: sessionToUid.keySet() ) {
            sendMessage(message, session);
        }
        return true;
    }
}
