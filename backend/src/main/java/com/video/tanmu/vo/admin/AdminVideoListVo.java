package com.video.tanmu.vo.admin;

import com.video.tanmu.model.VideoModel;
import com.video.tanmu.utils.ConvertUtils;
import lombok.Data;

import java.io.Serializable;
import java.text.SimpleDateFormat;

@Data
public class AdminVideoListVo implements Serializable {
    /**
     * 分类1
     */
    private Integer typeId1;

    private Integer typeId2;

    /**
     * 名称
     */
    private String name;

    /**
     * 图片
     */
    private String picture;
    /**
     * av
     */
    private String av;

    private String updateTime;

    public static AdminVideoListVo convertFromVideoModel(VideoModel videoModel) {
        if (null == videoModel) {
            return null;
        }
        AdminVideoListVo videoListVo = ConvertUtils.copyProperties(videoModel, AdminVideoListVo.class);
        String dateString = new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss").format (videoModel.getUpdateTime() * 1000);
        videoListVo.setUpdateTime(dateString);
        return videoListVo;
    }

}
