import json
import time

import requests
from flask import request, jsonify
from app.model.User import User
from app.model.Department import Department
from bson import ObjectId
from . import bp_user


@bp_user.route('/register', methods=['POST'])
def register():
    """注册"""
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    email = user_info.get("email")
    password = user_info.get("password")
    name = user_info.get("name")            # 企业名称
    role = user_info.get("type")

    user = User.objects(email=email).first()
    if user:
        return jsonify({"message": "The user already exists!"}), 400
    else:
        print(1)
        user = User(_id=ObjectId(),
                    email=user_info.get("email"),
                    password=password,
                    role=role)
        if role == "企业":
            user.enterprise_id = user._id
            # 注册根部门
            department = Department(_id=ObjectId(),
                                    deptName=name,
                                    enterprise_id=user.enterprise_id,
                                    orderNum=0,
                                    leader_id=user._id,
                                    phone=user.phone,
                                    createTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            department.save()

        user.save()
        return jsonify({})
