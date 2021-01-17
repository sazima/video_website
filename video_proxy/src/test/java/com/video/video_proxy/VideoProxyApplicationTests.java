package com.video.video_proxy;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import sun.awt.geom.AreaOp;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

//@SpringBootTest
class VideoProxyApplicationTests {

    @Test
    void contextLoads() throws URISyntaxException {
        String s = "#EXT-X-KEY:METHOD=AES-128,URI=key.key";
        Pattern p = Pattern.compile("URI=\"?(.*?)\"?");
        URI uri = new URI("http://ssssss.com:888/fdsfl/fdsaflj/fdasf.m3u8");
        Matcher m = p.matcher(s);
        while (m.find()) {
//                            request.getServletPath().append("?url=").append("URI=" + uri.resolve(m.group(1))
            String newUri = "URI=" + "http://baidu.com/proxy" + "?url=" + uri.resolve(m.group(1));
            s = s.replace(m.group(0), newUri);
        }
        System.out.println(s);
    }
}
