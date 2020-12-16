package com.video.tanmu.service;

import com.video.tanmu.model.UserModel;
import com.video.tanmu.param.UserCreateParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.LoginResponseVo;

public interface UserService {
    Response<Integer> insert(UserCreateParam userCreateParam);

    Response<LoginResponseVo> login(String email, String password);

    UserModel getUserByToken(String token);
}
