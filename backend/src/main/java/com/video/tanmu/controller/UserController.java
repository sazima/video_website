package com.video.tanmu.controller;

import com.video.tanmu.result.Response;
import com.video.tanmu.service.UserService;
import com.video.tanmu.vo.LoginResponseVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/user")
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    public Response<LoginResponseVo> login(String email, String password) {
        return userService.login(email, password);
    }

}
