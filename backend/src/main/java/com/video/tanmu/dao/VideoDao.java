package com.video.tanmu.dao;

import com.video.tanmu.model.Video;
import com.video.tanmu.param.VideoQueryParam;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface VideoDao {
    int deleteByPrimaryKey(Integer id);

    int insert(Video record);

    int insertSelective(Video record);

    Video selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(Video record);

    int updateByPrimaryKey(Video record);

    List<Video> selectByParentTypeId(@Param("parentTypeId")Integer parentTypeId, @Param("limit") Integer limit);

    List<Video> selectByQuery(VideoQueryParam videoQueryParam);

    Video selectByAv(@Param("av") String av);
}