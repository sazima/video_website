package com.video.tanmu.service.impl;

import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.redis.UserKey;
import com.video.tanmu.dao.UserDao;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.param.UserRegisterParam;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.UserService;
import com.video.tanmu.utils.AuthUtils;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.vo.LoginResponseVo;
import com.video.tanmu.vo.UserDetailVo;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.UUID;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserDao userDao;

    @Autowired
    private RedisClient redisClient;

    @Override
    public Response<Integer> register(UserRegisterParam userCreateParam) {
        if (StringUtils.isBlank(userCreateParam.getEmail())){
            return Response.fail("邮箱不能为空");
        }
        if (StringUtils.isBlank(userCreateParam.getNickName())){
            return Response.fail("昵称不能为空");
        }
        if (StringUtils.isBlank(userCreateParam.getPassword()) || userCreateParam.getPassword().length() < 6) {
            return Response.fail("密码太短");
        }
        UserModel userByUserName = userDao.selectByEmail(userCreateParam.getEmail());
        if (null != userByUserName) {
            return Response.fail("邮箱已存在");
        }
        UserModel userModel = new UserModel();
        userModel.setNickName(userCreateParam.getNickName());
        userModel.setPassword(AuthUtils.encrypt(userCreateParam.getPassword()));
        userModel.setEmail(userCreateParam.getEmail());
        userModel.setPicture(userCreateParam.getPicture());
        userModel.setAddTime(Instant.now().getEpochSecond());
        int inserted = userDao.insertSelective(userModel);
        return Response.success(inserted);
    }

    @Override
    public Response<LoginResponseVo> login(String email, String password) {
        UserModel userModel = userDao.selectByEmail(email);
        if (null == userModel) {
            return Response.fail("邮箱或者密码错误");
        }
        if (!AuthUtils.checkPassWorld(password, userModel.getPassword())) {
            return Response.fail("邮箱或者密码错误");
        }
        UserDetailVo userDetailVo = ConvertUtils.copyProperties(userModel, UserDetailVo.class);
        String token = UUID.randomUUID().toString().replaceAll("-", "");
        setTokenByUserId(userModel.getId(), token);
        return Response.success(new LoginResponseVo(userDetailVo, token));
    }

    @Override
    public UserModel getUserByToken(String token) {
        String key = UserKey.getTokenKey(token);
        Integer userId = redisClient.get(key, Integer.class);
        return getUserById(userId);
    }

    @Override
    public UserModel getUserAndRefreshToken(String token) {
        String key = UserKey.getTokenKey(token);
        Integer userId = redisClient.get(key, Integer.class);
        if (userId == null) {
            return null;
        }
        UserModel userById = getUserById(userId);
        if (null == userById) {
            return null;
        }
        redisClient.set(key, userId);
        return userById;
    }

    private void deleteTokenByUser(UserModel userModel) {

    }

    private void setTokenByUserId(Integer userId, String token) {
        redisClient.set(UserKey.getTokenKey(token), userId);
        List<String> tokenList = redisClient.getList(UserKey.getTokenListKey(userId), String.class);
        if (null != tokenList) {
            ArrayList<String> newTokenList = new ArrayList<>(tokenList);
            newTokenList.add(token);
            redisClient.set(UserKey.getTokenListKey(userId), newTokenList);
        } else {
            redisClient.set(UserKey.getTokenListKey(userId), Collections.singleton(token));
        }
    }

    private UserModel getUserById(Integer userId) {
        String key = UserKey.getUserByUserIdKey(userId);
        UserModel userCache = redisClient.get(key, UserModel.class);
        if (null != userCache) {
            return userCache;
        }
        UserModel userModel = userDao.selectByPrimaryKey(userId);
        redisClient.set(key, userModel);
        return userModel;
    }
}
