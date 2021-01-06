package com.video.tanmu.controller;

import com.video.tanmu.constants.ResponseCode;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.param.LoginParam;
import com.video.tanmu.param.UserRegisterParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.UserService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.vo.LoginResponseVo;
import com.video.tanmu.vo.UserDetailVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/user")
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @RequestMapping(value = "/login", method = RequestMethod.POST)
    @ResponseBody
    public Response<LoginResponseVo> login(@RequestBody LoginParam loginParam) {
        return userService.login(loginParam.getEmail(), loginParam.getPassword());
    }

    @RequestMapping(value = "/register", method = RequestMethod.POST)
    @ResponseBody
    public Response<Integer> insert(@RequestBody UserRegisterParam userRegisterParam) {
        return userService.register(userRegisterParam);
    }


    @RequestMapping("/loginStatus")
    public Response<UserDetailVo> getLoginStatus(UserModel userModel) {
        if (null == userModel) {
            return new Response(ResponseCode.NOT_LOGIN);
        }
        UserDetailVo userDetailVo = ConvertUtils.copyProperties(userModel, UserDetailVo.class);
        return Response.success(userDetailVo);
    }



}
