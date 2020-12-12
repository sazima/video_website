package com.video.tanmu.utils;

import org.springframework.beans.BeanUtils;
import org.springframework.util.CollectionUtils;

import java.util.ArrayList;
import java.util.List;

public class ConvertUtils<T> {
    public static <T> T copyProperties(Object source, Class<T> targetClass) {
        if (source == null) {
            return null;
        }
        try {
            T target = targetClass.newInstance();
            BeanUtils.copyProperties(source, target);
            return target;
        } catch (InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static <T> List<T> copyListProperties(List sources, Class<T> targetClass) {
        List<T> targetList = new ArrayList<>();
        if (CollectionUtils.isEmpty(sources)) {
            return targetList;
        }
        for (Object source : sources) {
            T target = copyProperties(source, targetClass);
            targetList.add(target);
        }
        return targetList;
    }

}
