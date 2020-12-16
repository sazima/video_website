package com.video.tanmu.controller;

import com.video.tanmu.param.LoginParam;
import com.video.tanmu.param.UserCreateParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.UserService;
import com.video.tanmu.vo.LoginResponseVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/user")
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @RequestMapping("/login")
    @ResponseBody
    public Response<LoginResponseVo> login(@RequestBody LoginParam loginParam) {
        return userService.login(loginParam.getEmail(), loginParam.getPassword());
    }

    @RequestMapping("/insert")
    @ResponseBody
    public Response<Integer> insert(@RequestBody UserCreateParam userCreateParam) {
        return userService.insert(userCreateParam);
    }


}
