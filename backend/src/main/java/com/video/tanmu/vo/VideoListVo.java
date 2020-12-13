package com.video.tanmu.vo;

import com.video.tanmu.model.VideoModel;
import com.video.tanmu.model.VideoTanmuModel;
import com.video.tanmu.utils.ConvertUtils;
import lombok.Data;

import java.text.SimpleDateFormat;
import java.util.Date;

@Data
public class VideoListVo {
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

    public static  VideoListVo convertFromVideoModel(VideoModel videoModel) {
        if (null == videoModel) {
            return null;
        }
        VideoListVo videoListVo = ConvertUtils.copyProperties(videoModel, VideoListVo.class);
        String dateString = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format (videoModel.getUpdateTime() * 1000);
        videoListVo.setUpdateTime(dateString);
        return videoListVo;
    }

}
