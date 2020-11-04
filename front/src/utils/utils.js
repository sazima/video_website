/* eslint-disable no-unused-vars */
import vue from "@/main";
import CryptoJS from 'crypto-js';

function isMobile() {
  let userAgentInfo = navigator.userAgent;
  let Agents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
  for (let v = 0; v < Agents.length; v++) {
    if (userAgentInfo.indexOf(Agents[v]) > 0) {
      return true
    }
  }
  return false;
}

function isIOS() {
    return [
            'iPad Simulator',
            'iPhone Simulator',
            'iPod Simulator',
            'iPad',
            'iPhone',
            'iPod'
        ].includes(navigator.platform)
        // iPad on iOS 13 detection
        || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
}

function toast(message, variant="danger", append = false) {
    vue.$bvToast.toast(message, {
        title: `提示`,
        toaster: 'b-toaster-top-center',
        appendToast: append,
        variant: variant,
        autoHideDelay: 3000
    })
}

function isEmptyObject(data) {
  if (!data) {
    return true
  }
  for (let i in data) {
    return false
  }
  return true
}

function requestFullScreen(ele) {
    if (document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement || document.msFullscreenElement) {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        }
    } else {
        if (ele.requestFullscreen) {
            ele.requestFullscreen();
        } else if (ele.mozRequestFullScreen) {
            ele.mozRequestFullScreen();
        } else if (ele.webkitRequestFullScreen) {
            ele.webkitRequestFullScreen();
        }
    }
}

function clearEventListener(element) {
  const clonedElement = element.cloneNode(true);
  element.replaceWith(clonedElement);
  return clonedElement;
}


function aes_encrypt(plaintext, key, iv) {
    key = CryptoJS.enc.Utf8.parse(key)
    iv = CryptoJS.enc.Utf8.parse(iv)
    let srcs = CryptoJS.enc.Utf8.parse(plaintext)
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    return encrypted.ciphertext.toString()
}

function aes_decrypt(ciphertext, key, iv) {
    key = CryptoJS.enc.Utf8.parse(key)
    iv = CryptoJS.enc.Utf8.parse(iv)
    let hex_string = CryptoJS.enc.Hex.parse(ciphertext)
    let srcs = CryptoJS.enc.Base64.stringify(hex_string)
    let decrypt = CryptoJS.AES.decrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    decrypt = decrypt.toString(CryptoJS.enc.Utf8)
    return decrypt.toString()
}

export {isMobile, isEmptyObject, requestFullScreen, clearEventListener, isIOS, toast, aes_decrypt, aes_encrypt}
