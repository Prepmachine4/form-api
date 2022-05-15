import json
from flask import request, jsonify
from app.model import User
from flask_jwt_extended import jwt_required
from . import bp_user

@bp_user.route('/profile', methods=['PUT'])
@jwt_required(optional=False)
def profile():
    '''修改用户信息'''
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