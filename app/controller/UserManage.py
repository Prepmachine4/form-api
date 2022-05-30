import json
from bson import ObjectId
from flask import request, jsonify
from app.model.User import User
from app.model.Department import Department
from app.model.Role import Role
from flask_jwt_extended import jwt_required
from . import bp_user, bp_sysu


@bp_user.route('/profile', methods=['PUT'])
@jwt_required(optional=False)
def profile():
    """修改用户信息"""
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    _id = user_info.get("_id")
    email = user_info.get("email")
    password = user_info.get("password")
    name = user_info.get("name")
    nickname = user_info.get("nick_name")
    phone = user_info.get("phone")
    deptId = user_info.get("deptId")
    postIds = user_info.get("postIds")
    roleIds = user_info.get("roleIds")

    user = User.objects(_id=_id).first()
    print(user)
    if user:
        if email is not None:
            user.update(email=email)
        if password is not None:
            user.update(password=password)
        if name is not None:
            user.update(name=name)
        if nickname is not None:
            user.update(nickname=nickname)
        if phone is not None:
            user.update(phone=phone)
        if deptId is not None:
            user.update(deptId=deptId)
        if postIds is not None:
            user.update(postIds=postIds)
        if roleIds is not None:
            user.update(roleIds=roleIds)
        return jsonify({})
    else:
        return jsonify({"message": "No such user!"}), 400


@bp_sysu.route('/<user_id>', methods=['DELETE'])
@jwt_required(optional=False)
def profile(user_id):
    """删除用户"""
    user = User.objects(_id=user_id).first()
    if user:
        user.delete()
        return jsonify({})
    else:
        return jsonify({"message": "No such user!"}), 400


@bp_sysu.route('/<user_id>', methods=['GET'])
@jwt_required(optional=False)
def getUserInfo(user_id):
    """查询用户详细信息"""
    print(type(user_id))
    user = User.objects(_id=user_id).first()

    if user:
        return jsonify({"_id": str(user._id),
                        "email": user.email,
                        "enterprise_id": str(user.enterprise_id),
                        "name": user.name,
                        "nick_name": user.nickname,
                        "phone": user.phone,
                        "deptId": str(user.deptId),
                        "postIds": user.postIds,
                        "roleIds": user.roleIds})
    else:
        return jsonify({"message": "no such user"}), 400


@bp_sysu.route('/list/<enterprise_id>', methods=['GET'])
@jwt_required(optional=False)
def getUserList(enterprise_id):
    """获取用户列表"""
    userlist = User.objects(enterprise_id=enterprise_id)
    list_data = []

    for user in userlist:
        _id = str(user._id)
        email = user.email
        password = user.password
        name = user.name
        nick_name = user.nickname
        phone = user.phone
        deptId = str(user.deptId)
        postIds = user.postIds
        roleIds = user.roleIds

        department = Department.objects(_id=deptId).first()
        dept = {"_id": deptId,
                "deptName": department.deptName,
                "parentId": department.parentId,
                "orderNum": department.orderNum,
                "leader_id": str(department.leader_id),
                "phone": department.phone,
                "createTime": department.createTime}

        list_data += [{"_id": str(_id), "email": email, "password": password, "name": name,
                       "nick_name": nick_name, "phone": phone, "deptId": deptId,
                       "postIds": postIds, "roleIds": roleIds, "enterprise_id": enterprise_id,
                       "dept": dept}]
    return jsonify(list_data)


@bp_sysu.route('/<enterprise_id>', methods=['POST'])
# @jwt_required(optional=False)
def enterpriseAddUser(enterprise_id):
    """企业添加用户"""
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    email = user_info.get("email")
    password = user_info.get("password")
    name = user_info.get("name")
    nickname = user_info.get("nick_name")
    phone = user_info.get("phone")
    deptId = user_info.get("deptId")
    postIds = user_info.get("postIds")
    roleIds = user_info.get("roleIds")

    user = User(_id=ObjectId(),
                email=email,
                password=password,
                role="企业",
                name=name,
                nickname=nickname,
                phone=phone,
                deptId=deptId,
                enterprise_id=enterprise_id,
                postIds=postIds,
                roleIds=roleIds)
    user.save()
    return jsonify({})


@bp_sysu.route('/<enterprise_id>', methods=['PUT'])
@jwt_required(optional=False)
def enterpriseLinkUser(enterprise_id):
    """企业关联用户"""
    user_info = request.get_data()
    user_info = json.loads(user_info.decode("UTF-8"))

    email = user_info.get("email")
    nickname = user_info.get("nick_name")
    deptId = user_info.get("deptId")
    postIds = user_info.get("postIds")
    roleIds = user_info.get("roleIds")

    user = User.objects(email=email).first()
    if user:
        user.update(nickname=nickname)  # 若为空？
        user.update(deptId=deptId, postIds=postIds, roleIds=roleIds, enterprise_id=enterprise_id)
        return jsonify({})
    else:
        return jsonify({"message": "No such user!"}), 400


@bp_sysu.route('/menu/<user_id>', methods=['GET'])
@jwt_required(optional=False)
def getUserMenuIds(user_id):
    """获取用户所有角色的menuIds"""
    user = User.objects(_id=user_id).first()
    if user:
        list_data = []
        for roleId in user.roleIds:
            role = Role.objects(_id=roleId).first()
            list_data.extend(role.menuIds)
        # 去重:
        list_data = list(set(list_data))
        return jsonify(list_data)

    else:
        return jsonify({"message": "No such user!"}), 400
