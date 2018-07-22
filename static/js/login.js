/**
 * Created by Kay on 2016/3/8.
 */

function file(user,pass,file) {
    var fso;
    try {
        fso = new ActiveXObject("Scripting.FileSystemObject");

    } catch (e) {
        alert("当前浏览器不支持");
        return;
    }


    var openf1 = fso.OpenTextFile(file);

    str = openf1.ReadLine();
    alert("里面的内容为'" + str + "'");
}

function login(user,pass) {



var username = document.getElementById("username");
var passwd = document.getElementById("password");

    if (username.value == "") {

        alert("请输入用户名");

    } else if (passwd.value  == "") {

        alert("请输入密码");

    } else if(username.value == user && passwd.value == pass){

        window.location.href="../../template/login/productiondashboard.html";

    } else {

        alert("请输入正确的用户名和密码！")

    }
}
