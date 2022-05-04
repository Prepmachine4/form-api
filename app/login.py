import json
from flask import Flask, request, jsonify, Blueprint
from flask_login import (current_user, LoginManager,
                         login_user, logout_user,
                         login_required)
from flask_mongoengine import MongoEngine
from app.models import user

bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理定义表单的相关路由

LoginManager.login_view = 'login'


@bp_form.route('/login', methods=['POST'])
def login():
    info = json.loads(request.data)
    # 通过邮箱和密码登录
    email = info.get('email')
    password = info.get('password', '')
    User = user.objects(email=email,
                        password=password).first()
    if User:
        login_user(User)
        return jsonify(User.to_json())
    else:
        return jsonify({"status": 401,
                        "reason": "Username or Password Error"})


@bp_form.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify(**{'result': 200,
                      'data': {'message': 'logout success'}})
