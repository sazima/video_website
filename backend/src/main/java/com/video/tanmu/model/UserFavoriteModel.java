package com.video.tanmu.model;

import java.io.Serializable;
import lombok.Data;

/**
 * user_favorite
 * @author 
 */
@Data
public class UserFavoriteModel implements Serializable {
    private Integer id;

    /**
     * 用户id
     */
    private Integer userId;

    /**
     * 视频av号码
     */
    private String av;

    /**
     * 视频名称
     */
    private String videoName;

    /**
     * 收藏时间
     */
    private Long addTime;

    private static final long serialVersionUID = 1L;
}