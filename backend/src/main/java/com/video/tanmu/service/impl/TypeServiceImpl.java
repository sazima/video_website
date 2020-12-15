package com.video.tanmu.service.impl;

import com.video.tanmu.dao.TypeDao;
import com.video.tanmu.model.TypeModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.TypeService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.Redis.RedisClient;
import com.video.tanmu.vo.TypeVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TypeServiceImpl implements TypeService {
    @Autowired
    private TypeDao typeDao;

    @Autowired
    private RedisClient redisClient ;

    @Override
    public Response<List<TypeVo>> selectAll() {
        String key = "allType";
        List<TypeVo> typeVosCache = redisClient.getList(key, TypeVo.class);
        if (typeVosCache!=null) {
            return Response.success(typeVosCache);
        }
        List<TypeModel> typeModels = typeDao.selectAll();
        List<TypeVo> typeVos = ConvertUtils.copyListProperties(typeModels, TypeVo.class);
        redisClient.set(key, typeVos);
        return Response.success(typeVos);
    }
}
