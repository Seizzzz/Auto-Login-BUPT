// ==UserScript==
// @name         Auto-Login-BUPT
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  自动登录北邮网关、身份认证系统
// @author       Seize
// @match        http://10.3.8.216/*
// @match        https://auth.bupt.edu.cn/*
// @grant        none
// ==/UserScript==

(function exec() {
    var _username = "";
    var _password = "";

    function loginNetwork() {
        var params = {
            "user": _username,
            "pass": _password
        };

        var form = document.createElement("form");
        form.action = window.location.href;
        form.method = "post";
        form.style.display = "none";

        for (var x in params) {
            var opt = document.createElement("textarea");
            opt.name = x;
            opt.value = params[x];
            form.appendChild(opt);
        }

        document.body.appendChild(form);
        form.submit();
    }

    function loginAuth() {
        var params = {
            "username": _username,
            "password": _password,
            "lt": document.getElementsByName("lt")[0].defaultValue,
            "execution": document.getElementsByName("execution")[0].defaultValue,
            "_eventId": document.getElementsByName("_eventId")[0].defaultValue,
            "rmShown": 1
        }

        var form = document.createElement("form");
        form.action = window.location.href;
        form.method = "post";
        form.style.display = "none";

        for (var x in params) {
            var opt = document.createElement("textarea");
            opt.name = x;
            opt.value = params[x];
            form.appendChild(opt);
        }

        document.body.appendChild(form);
        form.submit();
    }

    if(window.location.host.indexOf("auth.bupt.edu.cn") != -1) loginAuth();
    else if(window.location.host.indexOf("10.3.8.216") != -1) loginNetwork();
}())