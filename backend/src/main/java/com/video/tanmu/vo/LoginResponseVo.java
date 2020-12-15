package com.video.tanmu.vo;

import lombok.Data;

@Data
public class LoginResponseVo {
    private UserDetailVo userDetailVo;
    private String token;

    public LoginResponseVo() {}
    public LoginResponseVo(UserDetailVo userDetailVo, String token) {
        this.userDetailVo = userDetailVo;
        this.token = token;
    }
}
