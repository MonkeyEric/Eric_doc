# coding:utf-8
# register.py
users = [{'username': 'test', 'password': '123456'}]


def register(username, password1, password2):

    if not all([username, password1, password2]):
        return {"code": 0, "msg": "所有参数不能为空"}
    # 注册功能
    for user in users:
        if username == user['username']:
            return {"code": 0, "msg": "该用户名已存在！"}
    else:
        if password1 != password2:
            return {"code": 0, "msg": "两次密码输入不一致！"}
        else:
            if 6 <= len(username) >= 6 and 6 <= len(password1) <= 18:
                users.append({'username': username, 'password': password2})
                return {"code": 1, "msg": "注册成功"}
            else:
                return {"code": 0, "msg": "用户名和密码必须在6-18位之间"}