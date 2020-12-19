package com.video.tanmu.dao;

import com.video.tanmu.model.UserFavoriteModel;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface UserFavoriteDao {
    int deleteByPrimaryKey(Integer id);

    int insert(UserFavoriteModel record);

    int insertSelective(UserFavoriteModel record);

    UserFavoriteModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(UserFavoriteModel record);

    int updateByPrimaryKey(UserFavoriteModel record);

    List<String> selectAvListByUserId(@Param("userId") Integer userId);

    int removeByUserIdAndAv(@Param("userId") Integer userId, @Param("av")String av);
}