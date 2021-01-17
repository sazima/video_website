package com.video.video_proxy.filters;

import com.google.common.io.CharStreams;
import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;
import com.netflix.zuul.exception.ZuulException;
import lombok.SneakyThrows;
import org.apache.commons.lang.text.StrBuilder;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.springframework.cloud.netflix.zuul.filters.support.FilterConstants.POST_TYPE;
import static org.springframework.http.HttpStatus.INTERNAL_SERVER_ERROR;

public class ResponseFilter extends ZuulFilter {

    @Override
    public String filterType() {
        return POST_TYPE;
    }

    @Override
    public int filterOrder() {
        return 0;
    }

    @Override
    public boolean shouldFilter() {
        return true;
    }

    @SneakyThrows
    @Override
    public Object run() throws ZuulException {

        RequestContext context = RequestContext.getCurrentContext();

        HttpServletRequest request = context.getRequest();
        String urlString = request.getParameter("url");
        if (!urlString.endsWith("m3u8")) {
            return null;
        }
        try (final InputStream responseDataStream = context.getResponseDataStream()) {
            if (responseDataStream == null) {
                return null;
            }
            URI uri = new URI(urlString);
            String responseData = CharStreams.toString(new InputStreamReader(responseDataStream, "UTF-8"));
            String[] split = responseData.split("\n");
            StrBuilder strBuilder = new StrBuilder();
            for (String s : split) {
                if (s.startsWith("#")) {
                    if (s.startsWith("#EXT-X-KEY:")) {
                        Pattern p=Pattern.compile("URI=\"(.*?)\"");
                        Matcher m=p.matcher(s);
                        while(m.find()){
                            String newUri = "URI=\"" + request.getServletPath() + "?url=" + uri.resolve(m.group(1)) + "\"";
                            s = s.replace(m.group(0), newUri);
                        }
                    }
                    strBuilder.append(s);
                } else {
                    strBuilder.append(request.getServletPath()).append("?url=").append(uri.resolve(s).toString());
                }
                strBuilder.append("\n");
            }
            context.setResponseBody(strBuilder.toString());
            return null;
        } catch (Exception e) {
            throw new ZuulException(e, INTERNAL_SERVER_ERROR.value(), e.getMessage());
        }
    }
}