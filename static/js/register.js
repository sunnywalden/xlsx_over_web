document.write("<script type='text/javascript' src='md5.min.js'></script>");

function file(user,pass,file) {
    var fso;
    try {
        fso = new ActiveXObject("Scripting.FileSystemObject");

    } catch (e) {
        alert("当前浏览器不支持");
        return;
    }

    var f1 = fso.createtextfile(file, true);

    f1.write(user);
    f1.write(pass);
    var openf1 = fso.OpenTextFile(file);

    str = openf1.ReadLine();
    alert("里面的内容为'" + str + "'");
}

function register() {

    var flag = true;

    var username = document.getElementById("logname");
    var pass1 = document.getElementById("logpass");
    var pass2 = document.getElementById("logpass_again");

    if ( pass1 == pass2 ) {


        var sec_username = hex_md5(username);
        var sec_pass = hex_md5(pass1);

        file(sec_username,sec_pass,'users.dat')
    }
    else {
        alert("密码不匹配，请重新输入");
        flag = false
    }
    return flag
}
