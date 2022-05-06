import json
from flask import request, jsonify, Blueprint
from app.models import User
from bson import ObjectId

bp_user = Blueprint("user", __name__)  # 创建蓝图，该蓝图管理用户相关路由


@bp_user.route('/login', methods=['POST'])
def login():

    # 通过邮箱和密码登录
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    user = User.objects(email=form_info.get("email"),
                        password=form_info.get("password")).first()
    if user:
        return jsonify({"user_info": {"_id": str(user.id),
                                      "email": user.email,
                                      "role": user.role},
                        "token": "111"})
    else:
        return jsonify({"status": 401,
                        "reason": "Email or Password Error"})


@bp_user.route('/register', methods=['POST'])
def register():

    # 注册需要邮箱、密码、用户类型
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    user = User.objects(email=form_info.get("email")).first()
    if user:
        return jsonify({"status": 400,
                        "reason": "Email already exists"})
    else:
        user = User(_id=ObjectId(),
                    email=form_info.get("email"),
                    password=form_info.get("password"),
                    role=form_info.get("type"))
        user.save()
        return jsonify({"status": 200})
