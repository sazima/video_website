package com.video.tanmu.service;

import com.video.tanmu.model.UserModel;
import com.video.tanmu.result.Response;
import com.video.tanmu.vo.IndexTreeVo;

public interface IndexService {
    Response<IndexTreeVo> getIndexTree(UserModel userModel);
}
