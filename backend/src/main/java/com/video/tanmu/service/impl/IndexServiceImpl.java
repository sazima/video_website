package com.video.tanmu.service.impl;

import com.video.tanmu.dao.TypeDao;
import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.model.TypeModel;
import com.video.tanmu.model.UserModel;
import com.video.tanmu.model.VideoModel;
import com.video.tanmu.redis.RedisClient;
import com.video.tanmu.result.Response;
import com.video.tanmu.service.ConfigService;
import com.video.tanmu.service.IndexService;
import com.video.tanmu.utils.ConvertUtils;
import com.video.tanmu.vo.IndexTreeVo;
import com.video.tanmu.vo.TypeVo;
import com.video.tanmu.vo.TypeWithVideoListVo;
import com.video.tanmu.vo.VideoListVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class IndexServiceImpl implements IndexService {
    @Autowired
    private TypeDao typeDao;

    @Autowired
    private VideoDao videoDao;
    @Autowired
    private RedisClient redisClient;

    @Autowired
    private ConfigService configService;

    @Override
    public Response<IndexTreeVo> getIndexTree(UserModel userModel) {
        String key = "indexTreeVo";
        IndexTreeVo indexTreeVo = redisClient.get(key, IndexTreeVo.class);
        if (null == indexTreeVo) {
            indexTreeVo = new IndexTreeVo();
            List<TypeModel> allTypeModel = typeDao.selectAll();
            List<TypeVo> parentTypeList = new ArrayList<>();
            List<TypeWithVideoListVo> typeWithVideoListVoList = new ArrayList<>();
            for (TypeModel typeModel : allTypeModel) {
                if (!typeModel.getParentType().equals(0)) {
                    continue;
                }
                parentTypeList.add(ConvertUtils.copyProperties(typeModel, TypeVo.class));
                List<VideoModel> videoModels = videoDao.selectByTypeId(typeModel.getId(), 18);
                TypeWithVideoListVo typeWithVideoListVo = new TypeWithVideoListVo();
                typeWithVideoListVo.setTypeId(typeModel.getId());
                typeWithVideoListVo.setTypeName(typeModel.getName());
                List<VideoListVo> videoListVos = videoModels.stream().map(VideoListVo::convertFromVideoModel).collect(Collectors.toList());
                typeWithVideoListVo.setVideoListVos(videoListVos);
                typeWithVideoListVoList.add(typeWithVideoListVo);
            }
            indexTreeVo.setTypeVoList(parentTypeList);
            indexTreeVo.setTypeWithVideoListVoList(typeWithVideoListVoList);
            redisClient.set(key, indexTreeVo);
        }
        if (null != userModel) {
            return Response.success(indexTreeVo);
        }
        // 未登录用户显示一部分
        List<TypeWithVideoListVo> disPlayTypeListVo = new ArrayList<>();

        List<Integer> noLoginTypeId = configService.getNoLoginTypeId();
        for (TypeWithVideoListVo typeWithVideoListVo : indexTreeVo.getTypeWithVideoListVoList()) {
            if (!noLoginTypeId.contains(typeWithVideoListVo.getTypeId())) {
                disPlayTypeListVo.add(typeWithVideoListVo);
            }
        }
        indexTreeVo.setTypeWithVideoListVoList(disPlayTypeListVo);
        return Response.success(indexTreeVo);
    }
}
