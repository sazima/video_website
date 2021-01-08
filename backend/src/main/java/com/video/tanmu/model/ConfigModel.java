package com.video.tanmu.model;

import lombok.Data;

import java.io.Serializable;

@Data
public class ConfigModel implements Serializable {
    private Integer id;

    /**
     * key
     */
    private String name;

    private String value;

    private static final long serialVersionUID = 1L;
}