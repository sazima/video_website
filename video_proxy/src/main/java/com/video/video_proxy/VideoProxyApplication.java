package com.video.video_proxy;

import com.video.video_proxy.filters.ResponseFilter;
import com.video.video_proxy.filters.RequestFilter;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
@EnableZuulProxy
public class VideoProxyApplication {

	public static void main(String[] args) {
		SpringApplication.run(VideoProxyApplication.class, args);
	}

	@Bean
	public RequestFilter simpleFilter() {
		return new RequestFilter();
	}

	@Bean
	public ResponseFilter responseFilter() {
		return new ResponseFilter();
	}
}
