import json
from flask import request, jsonify, Blueprint
from app.models import User
from bson import ObjectId
from flask_jwt_extended import create_access_token,jwt_required

bp_user = Blueprint("user", __name__)  # 创建蓝图，该蓝图管理用户相关路由


@bp_user.route('/login', methods=['POST'])
def login():
    # 通过邮箱和密码登录
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    user = User.objects(email=user_info.get("email"),
                        password=user_info.get("password")).first()
    if user:
        return jsonify({"user_info": {"_id": str(user._id),
                                      "email": user.email,
                                      "role": user.role},
                        "token": create_access_token(identity=user.email)})
    else:
        return jsonify({"message":"Email or password error!"}), 400


@bp_user.route('/register', methods=['POST'])
def register():
    # 注册需要邮箱、密码、用户类型
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    user = User.objects(email=user_info.get("email")).first()
    if user:
        return jsonify({"message":"The user already exists!"}), 400
    else:
        user = User(_id=ObjectId(),
                    email=user_info.get("email"),
                    password=user_info.get("password"),
                    role=user_info.get("type"),
                    nickname="")
        user.save()
        return jsonify({})


@bp_user.route('/profile', methods=['PUT'])
@jwt_required(optional=False)
def profile():
    # 修改密码，传入email、nickname、password
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    email = user_info.get("email")
    password = user_info.get("password")
    nickname = user_info.get("nick_name")

    user = User.objects(email=email).first()
    if user:
        user.update(password=password)
        if nickname != None:
            user.update(nickname=nickname)
        return jsonify({})
    else:
        return jsonify({"message": "No such user!"}), 400
