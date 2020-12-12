package com.video.tanmu.service.impl;

import com.video.tanmu.dao.TypeDao;
import com.video.tanmu.dao.VideoDao;
import com.video.tanmu.model.Type;
import com.video.tanmu.model.Video;
import com.video.tanmu.result.Response;
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

@Service
public class IndexServiceImpl implements IndexService {
    @Autowired
    private TypeDao typeDao;

    @Autowired
    private VideoDao videoDao;

    @Override
    public Response<IndexTreeVo> getIndexTree() {
        IndexTreeVo indexTreeVo = new IndexTreeVo();
        List<Type> allType = typeDao.selectAll();
        List<TypeVo> parentTypeList = new ArrayList<>();
        List<TypeWithVideoListVo> typeWithVideoListVoList = new ArrayList<>();

        for (Type type : allType) {
            if (!type.getParentType().equals(0)) {
                 continue;
            }
            parentTypeList.add(ConvertUtils.copyProperties(type, TypeVo.class));
            List<Video> videos = videoDao.selectByParentTypeId(type.getId(), 36);
            TypeWithVideoListVo typeWithVideoListVo = new TypeWithVideoListVo();
            typeWithVideoListVo.setTypeId(type.getId());
            typeWithVideoListVo.setTypeName(type.getName());
            typeWithVideoListVo.setVideoListVos(ConvertUtils.copyListProperties(videos, VideoListVo.class));
            typeWithVideoListVoList.add(typeWithVideoListVo);
        }
        indexTreeVo.setTypeVoList(parentTypeList);
        indexTreeVo.setTypeWithVideoListVoList(typeWithVideoListVoList);
        return Response.success(indexTreeVo);
    }
}
