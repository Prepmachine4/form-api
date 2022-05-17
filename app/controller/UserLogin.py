import json
from flask import request, jsonify
from app.model.User import User
from flask_jwt_extended import create_access_token
from . import bp_user


@bp_user.route('/login', methods=['POST'])
def login():
    """登录"""
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    user = User.objects(email=user_info.get("email"),
                        password=user_info.get("password")).first()
    if user:
        return jsonify({"user_info": {"_id": str(user._id),
                                      "email": user.email,
                                      "role": user.role},
                        "token": create_access_token(identity=str(user._id))})
    else:
        return jsonify({"message": "Email or password error!"}), 400
