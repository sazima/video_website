package com.video.tanmu.model;

import java.io.Serializable;
import lombok.Data;

/**
 * user
 * @author 
 */
@Data
public class UserModel implements Serializable {
    private Integer id;

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

    private Long addTime;

    /**
     * 状态
     */
    private Integer status;

    private static final long serialVersionUID = 1L;
}