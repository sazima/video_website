package com.video.tanmu.controller;

import com.video.tanmu.result.Response;
import com.video.tanmu.service.TypeService;
import com.video.tanmu.vo.TypeVo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequestMapping("/type")
@RestController
public class TypeController {
    @Autowired
    private TypeService typeService;

    @RequestMapping("/getAll")
    public Response<List<TypeVo>> getAll() {
        return typeService.selectAll();
    }
}
