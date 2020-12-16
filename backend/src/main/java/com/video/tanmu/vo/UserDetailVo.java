package com.video.tanmu.vo;

import lombok.Data;

@Data
public class UserDetailVo {

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

    private Long addTime;
}
