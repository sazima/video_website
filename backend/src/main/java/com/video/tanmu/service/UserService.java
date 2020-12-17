package com.video.tanmu.service;

import com.video.tanmu.model.UserModel;
import com.video.tanmu.param.UserRegisterParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.LoginResponseVo;

public interface UserService {
    Response<Integer> register(UserRegisterParam userCreateParam);

    Response<LoginResponseVo> login(String email, String password);

    UserModel getUserByToken(String token);

    UserModel getUserAndRefreshToken(String token);
}
