verify_register = function () {
    var username = document.forms['register']['username'].value;
    var password = document.forms['register']['password'].value;
    if (username == null || username == '' || username.replace(/(^\s*)|(\s*$)/g, "") == "") {
        alert('姓名为空');
        return;
    }
    if (username.replace(/\w/g, '') != '') {
        alert('用户名由字母、数字和下划线构成');
        return;
    }
    if (username.length < 4 || username.length > 20) {
        alert('用户名长度为4-20个字符');
        return;
    }
    if (password == null || password == '' || password.replace(/(^\s*)|(\s*$)/g, "") == "") {
        alert('密码不能为空');
        return;
    }
    if (password.length < 4 || password.length > 20) {
        alert('无效的密码，密码长度必须在4~20之间');
        return;
    }
}

verify_login = function () {
    var username = document.forms['login']['username'].value;
    var password = document.forms['login']['password'].value;
    if (username == null || username == '' || username.replace(/(^\s*)|(\s*$)/g, "") == "") {
        alert('姓名为空');
        return;
    }
    if (username.replace(/\w/g, '') != '') {
        alert('用户名由字母、数字和下划线构成');
        return;
    }
    if (username.length < 4 || username.length > 20) {
        alert('用户名长度为4-20个字符');
        return;
    }
    if (password == null || password == '' || password.replace(/(^\s*)|(\s*$)/g, "") == "") {
        alert('密码不能为空');
        return;
    }
    if (password.length < 4 || password.length > 20) {
        alert('无效的密码，密码长度必须在4~20之间');
        return;
    }
}

display_weapons = function (e) {
    $.ajax({
        type: 'get',
        url: '/weapon/weapons/' + e.id,
        dataType: 'json',
        success: function (data, status) {
            console.log(data);
            var d = data['data'];
            var str = '';
            for (var i = 0; i < d.length; i++) {
                str += '<li>' + d[i] + '</li>'
            }
            document.getElementById('display').innerHTML = str;
        }
    })
}

