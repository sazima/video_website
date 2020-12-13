package com.video.tanmu.dao;

import com.video.tanmu.model.TypeModel;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface TypeDao {
    int deleteByPrimaryKey(Integer id);

    int insert(TypeModel record);

    int insertSelective(TypeModel record);

    TypeModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(TypeModel record);

    int updateByPrimaryKey(TypeModel record);

    List<TypeModel> selectAll();
}