package com.video.video_proxy.filters;

import com.netflix.zuul.ZuulFilter;
import com.netflix.zuul.context.RequestContext;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.cloud.netflix.zuul.filters.support.FilterConstants;

import javax.servlet.http.HttpServletRequest;
import java.net.MalformedURLException;
import java.net.URL;

public class SimpleFilter extends ZuulFilter {

    private static Logger log = LoggerFactory.getLogger(SimpleFilter.class);

    @Override
    public String filterType() {
        return FilterConstants.PRE_TYPE;
    }

    @Override
    public int filterOrder() {
        return FilterConstants.SEND_FORWARD_FILTER_ORDER;
    }

    @Override
    public boolean shouldFilter() {
        return true;
    }

    @lombok.SneakyThrows
    @Override
    public Object run() {
        RequestContext ctx = RequestContext.getCurrentContext();
        HttpServletRequest request = ctx.getRequest();
        String servletPath = request.getServletPath();
        // todo 验证
        String url = servletPath.replaceAll("/proxy/", "").replaceAll("//", "/").replaceAll("https:/", "https://").replaceAll("http:/", "http://");
        if (!url.startsWith("http")) {
            throw new Exception("xxx");
        }
        try {
            ctx.setRouteHost(new URL(url));
            ctx.set("requestURI", "");
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        return null;
    }

}