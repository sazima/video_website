package com.video.tanmu.dao;

import com.video.tanmu.model.VideoLink;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface VideoLinkDao {
    int deleteByPrimaryKey(Integer id);

    int insert(VideoLink record);

    int insertSelective(VideoLink record);

    VideoLink selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(VideoLink record);

    int updateByPrimaryKey(VideoLink record);

    List<VideoLink> selectByVideoId(@Param("videoId") Integer videoId);
}