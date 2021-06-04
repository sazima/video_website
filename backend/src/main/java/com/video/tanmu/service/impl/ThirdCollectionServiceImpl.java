package com.video.tanmu.service.impl;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;
import com.video.tanmu.dao.ThirdCollectionApiDao;
import com.video.tanmu.dao.TypeDao;
import com.video.tanmu.model.ThirdCollectionApiModel;
import com.video.tanmu.model.TypeModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ThirdCollectionService;
import com.video.tanmu.vo.ThirdCollectionApiVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@Service
public class ThirdCollectionServiceImpl implements ThirdCollectionService {
    @Autowired
    private ThirdCollectionApiDao thirdCollectionApiDao;

    @Autowired
    private TypeDao typeDao;

    @Override
    public Response<List<ThirdCollectionApiVo>> selectAll() {
        List<ThirdCollectionApiModel> thirdCollectionApis = thirdCollectionApiDao.selectAll();
        List<TypeModel> allType = typeDao.selectAll();
        HashMap<Integer, TypeModel> typeIdToType = new HashMap<>();
        for (TypeModel type : allType) {
            typeIdToType.put(type.getId(), type);
        }
        List<ThirdCollectionApiVo> thirdCollectionApiVos = new ArrayList<>();
        for (ThirdCollectionApiModel model : thirdCollectionApis) {
            thirdCollectionApiVos.add(convertToVo(model, typeIdToType));
        }
        return  Response.success(thirdCollectionApiVos);
    }

    @Override
    public Response<Integer> updateOrCreate(ThirdCollectionApiVo thirdCollectionApiVo) {
        ThirdCollectionApiModel model = convertToModel(thirdCollectionApiVo);
        if (null != model.getId()) {
            thirdCollectionApiDao.updateByPrimaryKey(model);
        } else {
            thirdCollectionApiDao.insert(model);
        }
        return Response.success(model.getId());
    }

    private ThirdCollectionApiVo convertToVo(ThirdCollectionApiModel model, HashMap<Integer, TypeModel> typeIdToType) {
            ThirdCollectionApiVo thirdCollectionApiVo = new ThirdCollectionApiVo();
            thirdCollectionApiVo.setId(model.getId());
            thirdCollectionApiVo.setKey(model.getKey());
            thirdCollectionApiVo.setUrl(model.getUrl());
            thirdCollectionApiVo.setName(model.getName());
            List<ThirdCollectionApiVo.BindIdVo> bindIdVos = JSON.parseArray(model.getBindId(), ThirdCollectionApiVo.BindIdVo.class);
            for (ThirdCollectionApiVo.BindIdVo bindIdVo: bindIdVos) {
                TypeModel typeModel = typeIdToType.get(bindIdVo.getSystemId());
                if (null != typeModel) {
                    bindIdVo.setTypeName(typeModel.getName());
                } else {
                    bindIdVo.setTypeName("");
                }
            }
            thirdCollectionApiVo.setBindId(bindIdVos);
            return thirdCollectionApiVo;
    }

    private ThirdCollectionApiModel convertToModel(ThirdCollectionApiVo vo) {
        ThirdCollectionApiModel model = new ThirdCollectionApiModel();
        model.setId(vo.getId());
        model.setName(vo.getName());
        model.setKey(vo.getKey());
        model.setUrl(vo.getUrl());
        model.setBindId(JSON.toJSONString(vo.getBindId(), SerializerFeature.WriteMapNullValue));
        return model;
    }
}
