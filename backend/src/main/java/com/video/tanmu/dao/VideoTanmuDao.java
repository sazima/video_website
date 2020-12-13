package com.video.tanmu.dao;

import com.video.tanmu.model.VideoTanmuModel;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface VideoTanmuDao {
    int deleteByPrimaryKey(Integer id);

    int insert(VideoTanmuModel record);

    int insertSelective(VideoTanmuModel record);

    VideoTanmuModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(VideoTanmuModel record);

    int updateByPrimaryKey(VideoTanmuModel record);

    List<VideoTanmuModel> selectByVideo(@Param("videoId") Integer videoId,
                                        @Param("fromName")String fromName,
                                        @Param("playName") String playName );
}