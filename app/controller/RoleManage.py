from flask import request, json
from app.model.Role import Role
from bson import ObjectId
from . import bp_role


@bp_role.route('/list/<enterprise_id>', methods=['GET'])
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
        menuTree = role.menuTree
        createTime = role.createTime
        menuIds = role.menuIds

        list_data += [{"_id": _id, "enterprise_id": enterprise_id, "roleName": roleName,
                       "roleKey": roleKey, "roleSort": roleSort, "admin": admin,
                       "menuTree": menuTree, "createTime": createTime, "menuIds": menuIds}]

    return json.jsonify(list_data)


@bp_role.route('/<enterprise_id>', methods=['POST'])
def addRole(enterprise_id):
    """新增角色"""
    role_info = request.get_data()
    role_info = json.loads(role_info.decode("UTF-8"))

    roleName = role_info.get("roleName")
    roleKey = role_info.get("roleKey")
    roleSort = role_info.get("roleSort")
    admin = role_info.get("admin")
    menuTree = role_info.get("menuTree")
    createTime = role_info.get("createTime")
    menuIds = role_info.get("menuIds")

    role = Role(_id=ObjectId(),
                roleName=roleName,
                enterprise_id=enterprise_id,
                roleKey=roleKey,
                roleSort=roleSort,
                admin=admin,
                menuTree=menuTree,
                createTime=createTime,
                menuIds=menuIds)

    role.save()

    return json.jsonify({})


@bp_role.route('/<role_id>', methods=['DELETE'])
def deleteRole(role_id):
    """删除角色"""
    Role.objects(_id=role_id).delete()

    return json.jsonify({})


@bp_role.route('/<role_id>', methods=['GET'])
def getRoleInfo(role_id):
    """获取角色详细信息"""
    role = Role.objects(_id=role_id).first()

    _id = str(role._id)
    roleName = role.roleName
    roleKey = role.roleKey
    roleSort = role.roleSort
    admin = role.admin
    menuTree = role.menuTree
    createTime = role.createTime
    menuIds = role.menuIds

    return json.jsonify({"_id": _id, "roleName": roleName,
                         "roleKey": roleKey, "roleSort": roleSort, "admin": admin,
                         "menuTree": menuTree, "createTime": createTime, "menuIds": menuIds})
