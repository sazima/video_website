package com.video.tanmu.dao;

import com.video.tanmu.model.ThirdCollectionApiModel;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
public interface ThirdCollectionApiDao {
    int deleteByPrimaryKey(Integer id);

    int insert(ThirdCollectionApiModel record);

    int insertSelective(ThirdCollectionApiModel record);

    ThirdCollectionApiModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(ThirdCollectionApiModel record);

    int updateByPrimaryKey(ThirdCollectionApiModel record);

    List<ThirdCollectionApiModel> selectAll();
}