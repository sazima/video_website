package com.video.tanmu.service;

import com.video.tanmu.result.Response;

public interface ShareScreenService {
    Response<String> generateUid();

    Response<Boolean> checkUid(String uid);
}
