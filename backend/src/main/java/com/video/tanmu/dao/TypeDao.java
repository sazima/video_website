package com.video.tanmu.dao;

import com.video.tanmu.model.Type;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
public interface TypeDao {
    int deleteByPrimaryKey(Integer id);

    int insert(Type record);

    int insertSelective(Type record);

    Type selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(Type record);

    int updateByPrimaryKey(Type record);

    List<Type> selectAll();
}