package com.video.tanmu.service;

import java.util.List;

public interface ConfigService {
    List<String> getRandomTanmuList();

    //
    List<Integer> getNoLoginTypeId();

    List<String> getProxyPrefixList();

    Boolean getRegisterSwitch();
}
