from flask import request, json
from app.model.Role import Role
from bson import ObjectId
import time
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_role


@bp_role.route('/list/<enterprise_id>', methods=['GET'])
@jwt_required(optional=False)
def getAllRole(enterprise_id):
    """获取所有角色"""
    role_list = Role.objects(enterprise_id=enterprise_id)
    list_data = []

    for role in role_list:
        _id = str(role._id)
        enterprise_id = str(role.enterprise_id)
        roleName = role.roleName
        roleKey = role.roleKey
        roleSort = role.roleSort
        admin = role.admin
        dataScope = role.dataScope
        createTime = role.createTime
        menuIds = role.menuIds

        list_data += [{"_id": _id, "enterprise_id": enterprise_id, "roleName": roleName,
                       "roleKey": roleKey, "roleSort": roleSort, "admin": admin,
                       "dataScope": dataScope, "createTime": createTime, "menuIds": menuIds}]
    return json.jsonify(list_data)


@bp_role.route('/<enterprise_id>', methods=['POST'])
@jwt_required(optional=False)
def addRole(enterprise_id):
    """新增角色"""
    role_info = request.get_data()
    role_info = json.loads(role_info.decode("UTF-8"))

    roleName = role_info.get("roleName")
    roleKey = role_info.get("roleKey")
    roleSort = role_info.get("roleSort")
    menuIds = role_info.get("menuIds")
    admin = False
    dataScope = ""
    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    role = Role(_id=ObjectId(),
                roleName=roleName,
                enterprise_id=enterprise_id,
                roleKey=roleKey,
                roleSort=roleSort,
                admin=admin,
                dataScope=dataScope,
                createTime=createTime,
                menuIds=menuIds)

    role.save()

    return json.jsonify({})


@bp_role.route('/<role_id>', methods=['DELETE'])
@jwt_required(optional=False)
def deleteRole(role_id):
    """删除角色"""
    Role.objects(_id=role_id).delete()

    return json.jsonify({})


@bp_role.route('/<role_id>', methods=['GET'])
@jwt_required(optional=False)
def getRoleInfo(role_id):
    """获取角色详细信息"""
    role = Role.objects(_id=role_id).first()

    _id = str(role._id)
    roleName = role.roleName
    roleKey = role.roleKey
    roleSort = role.roleSort
    admin = role.admin
    dataScope = role.dataScope
    createTime = role.createTime
    menuIds = role.menuIds

    return json.jsonify({"_id": _id, "roleName": roleName,
                         "roleKey": roleKey, "roleSort": roleSort, "admin": admin,
                         "dataScope": dataScope, "createTime": createTime, "menuIds": menuIds})


@bp_role.route('/dataScope', methods=['PUT'])
@jwt_required(optional=False)
def SetRoleAuth():
    """赋予角色数据权限"""
    role_info = request.get_data()
    role_info = json.loads(role_info.decode("UTF-8"))

    _id = role_info.get("_id")
    dataScope = role_info.get("dataScope")

    role = Role.objects(_id=_id).first()
    role.update(dataScope=dataScope)

    return json.jsonify({})
