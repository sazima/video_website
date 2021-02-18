export default {
    ws: null,
    getHostByUrl(url) {
        document.createElement ('a')
            let tmp        = document.createElement ('a');
         tmp.href   = url
         return tmp.host
    },
    getWebsocketUrl(uid) {
        let wsUrl = "";
        const baseUrl = process.env.VUE_APP_BASE_URL || window.location.protocol + "://" + window.location.host
        if (baseUrl.startsWith("https")) {
            wsUrl += 'wss://'
        } else {
            wsUrl += 'ws://'
        }
        wsUrl += this.getHostByUrl(baseUrl) + '/api/ws?uid=' + uid
        return wsUrl
    },
    createWebsocket(uid) {
        if (this.ws) {
            return this.ws;
        }
        console.log(this.getWebsocketUrl(uid));
        if ("WebSocket" in window) {
            this.ws = new WebSocket(this.getWebsocketUrl(uid));
            this.ws.onopen =  () => {
                console.log('websocket连接成功');
                this.ws.send(JSON.stringify({
                    "type": 'hello'
                }))
            };
            this.ws.onclose =  () => {
                console.log("连接已关闭...");
                this.ws = null;
                setTimeout(() => {
                    this.createWebsocket(uid);
                }, 2000);
            };
        } else {
            console.log("您的浏览器不支持 WebSocket!");
        }
        return this.ws
    },
    getWebsocket(uid) {
        if (this.ws) {
            return this.ws
        } else {
            return this.createWebsocket(uid)
        }
    }
}
