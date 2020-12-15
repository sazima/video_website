package com.video.tanmu.utils;

public class AuthUtils {

    public static String encrypt(String password) {
        // todo
        return password;
    }

    public static boolean checkPassWorld(String password, String encryptPassword) {
        return password.equals(encryptPassword);
    }


}
