package com.video.tanmu.result;

import com.video.tanmu.constants.ResponseCode;
import lombok.Data;

import java.io.Serializable;

@Data
public class Response<T> implements Serializable {
    private Integer code;
    private String msg;
    private T data;

    Response(){}
    Response(T data, ResponseCode responseCode) {
        this.data = data;
        this.code = responseCode.getCode();
        this.msg = responseCode.getMsg();
    }

    public Response(ResponseCode responseCode){
        this.code = responseCode.getCode();
        this.msg = responseCode.getMsg();
    }

    public static<T> Response<T> success(T data) {
        return new Response<>(data, ResponseCode.SUCCESS);
    }

    public static<T>  Response<T> fail(String msg) {
        Response<T> response = new Response<>();
        response.setCode(ResponseCode.FAIL.getCode());
        response.setMsg(msg);
        return response;
    }
}
