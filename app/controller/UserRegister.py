import json
from flask import request, jsonify
from app.model.User import User
from bson import ObjectId
from . import bp_user

@bp_user.route('/register', methods=['POST'])
def register():
    '''注册'''
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