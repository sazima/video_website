package com.video.tanmu.dao;

import com.video.tanmu.model.VideoLinkModel;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface VideoLinkDao {
    int deleteByPrimaryKey(Integer id);

    int insert(VideoLinkModel record);

    int insertSelective(VideoLinkModel record);

    VideoLinkModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(VideoLinkModel record);

    int updateByPrimaryKey(VideoLinkModel record);

    List<VideoLinkModel> selectByVideoId(@Param("videoId") Integer videoId);

    VideoLinkModel selectByFromAndName(@Param("fromName") String fromName,
                                       @Param("playUrl")String playUrl);
}