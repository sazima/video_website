package com.video.tanmu.dao;

import com.video.tanmu.model.VideoModel;
import com.video.tanmu.param.VideoQueryParam;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface VideoDao {
    int deleteByPrimaryKey(Integer id);

    int insert(VideoModel record);

    int insertSelective(VideoModel record);

    VideoModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(VideoModel record);

    int updateByPrimaryKey(VideoModel record);

    List<VideoModel> selectByTypeId(@Param("typeId")Integer typeId, @Param("limit") Integer limit);

    List<VideoModel> selectByQuery(@Param("videoQueryParam") VideoQueryParam videoQueryParam,
                                   @Param("offset") Integer offset,
                                   @Param("limit") Integer limit,
                                   @Param("exceptTypeList") List<Integer>exceptTypeList);

    int selectTotalByQuery(VideoQueryParam videoQueryParam);

    VideoModel selectByAv(@Param("av") String av);

    List<VideoModel> selectByAvList(@Param("avList") List<String> avList);
}