package com.video.tanmu.dao;

import com.video.tanmu.model.ConfigModel;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface ConfigDao {
    int deleteByPrimaryKey(Integer id);

    int insert(ConfigModel record);

    int insertSelective(ConfigModel record);

    ConfigModel selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(ConfigModel record);

    int updateByPrimaryKey(ConfigModel record);
    
    ConfigModel selectByName(String name);
}