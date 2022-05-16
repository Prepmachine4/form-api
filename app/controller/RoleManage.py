from flask import request, json
from app.model.Role import Role
from bson import ObjectId
from flask import Blueprint

bp_role = Blueprint("role", __name__)  # 创建蓝图，该蓝图管理角色的相关路由

@bp_role.route('/list/<enterprise_id>', methods=['GET'])
def getAllRole(enterprise_id):
    '''获取所有角色'''
    return json.jsonify({})


@bp_role.route('/<enterprise_id>', methods=['POST'])
def addRole(enterprise_id):
    '''新增角色'''
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