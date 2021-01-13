package com.video.tanmu.service.impl;

import com.alibaba.fastjson.JSON;
import com.video.tanmu.constants.SystemConfigNameConstants;
import com.video.tanmu.dao.ConfigDao;
import com.video.tanmu.model.ConfigModel;
import com.video.tanmu.redis.ConfigKey;
import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.service.ConfigService;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ConfigServiceImpl implements ConfigService {
    @Autowired
    private RedisClient redisClient;

    @Autowired
    private ConfigDao configDao;


    @Override
    public List<String> getRandomTanmuList() {
        String value = getValueByName(SystemConfigNameConstants.RANDOM_TANMU_LIST);
        if (StringUtils.isEmpty(value)) {
            return new ArrayList<>();
        }
        return JSON.parseArray(value, String.class);
    }

    //
    @Override
    public List<Integer> getNoLoginTypeId() {
        String value = getValueByName(SystemConfigNameConstants.NEED_LOGIN_TYPE_ID);
        if (StringUtils.isEmpty(value)) {
            return new ArrayList<>();
        }
        return JSON.parseArray(value, Integer.class);
    }

    @Override
    public List<String> getProxyPrefixList() {
        String value = getValueByName(SystemConfigNameConstants.PROXY_SERVER_PREFIX);
        if (StringUtils.isEmpty(value)) {
            return new ArrayList<>();
        }
        return JSON.parseArray(value, String.class);
    }

    @Override
    public Boolean getRegisterSwitch() {
        String value = getValueByName(SystemConfigNameConstants.REGISTER_SWITCH);
        return value.equals("true");
    }
    private String getValueByName(String name) {
        String key = ConfigKey.getRedisKeyByName(name);
        String value = redisClient.get(key, String.class);
        if (null == value) {
            ConfigModel configModel = configDao.selectByName(name);
            if (null == configModel) {
                value = "";
            } else {
                value = configModel.getValue();
            }
            redisClient.set(key, value);
        }
        return value;
    }
}
