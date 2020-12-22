package com.video.tanmu.controller;

import com.video.tanmu.model.UserModel;
import com.video.tanmu.result.Response;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/userFavorite")
public class UserFavoriteController {
    @RequestMapping("/add")
    @ResponseBody
    public Response<Integer> addFavoriteVideo(UserModel userModel) {
        return null;
    }

}
