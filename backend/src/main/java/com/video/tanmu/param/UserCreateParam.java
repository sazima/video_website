package com.video.tanmu.param;

import lombok.Data;

@Data
public class UserCreateParam {
    /**
     * 昵称
     */
    private String nickName;

    /**
     * 邮箱
     */
    private String email;

    /**
     * 头像
     */
    private String picture;

    /**
     * 密码
     */
    private String password;

}
