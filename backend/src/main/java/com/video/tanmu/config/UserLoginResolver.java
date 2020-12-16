package com.video.tanmu.config;

import com.video.tanmu.Redis.RedisClient;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.service.UserService;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.MethodParameter;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.support.WebDataBinderFactory;
import org.springframework.web.context.request.NativeWebRequest;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.method.support.ModelAndViewContainer;

import javax.servlet.http.HttpServletRequest;

@Service
public class UserLoginResolver implements HandlerMethodArgumentResolver {
    private final String TOKEN_NAME = "token";

    @Autowired
    private UserService userService;


    @Override
    public boolean supportsParameter(MethodParameter methodParameter) {
        Class<?> clazz = methodParameter.getParameterType();
        return UserModel.class == clazz;
    }

    @Override
    public UserModel resolveArgument(MethodParameter methodParameter,
                                  ModelAndViewContainer modelAndViewContainer,
                                  NativeWebRequest nativeWebRequest,
                                  WebDataBinderFactory webDataBinderFactory) throws Exception {

        HttpServletRequest request = nativeWebRequest.getNativeRequest(HttpServletRequest.class);
        String token = request.getHeader(TOKEN_NAME);
        if (StringUtils.isBlank(token)) {
            return null;
        }
        return userService.getUserByToken(token);
    }
}
