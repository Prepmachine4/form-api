import time
from flask import request, json
from bson import ObjectId
from app.model.Department import Department
from app.model.User import User
from flask_jwt_extended import jwt_required
from . import bp_dept


@bp_dept.route('/list/<enterprise_id>', methods=['GET'])
@jwt_required(optional=False)
def getAllDepartments(enterprise_id):
    """获取所有部门"""
    department_list = Department.objects(enterprise_id=enterprise_id)
    list_data = []

    for department in department_list:
        _id = department._id
        deptName = department.deptName
        parentId = department.parentId
        orderNum = department.orderNum
        leader_id = department.leader_id
        phone = department.phone
        createTime = department.createTime
        roleIds = department.roleIds

        leader = User.objects(_id=str(leader_id)).first()
        leader_name = leader.name

        list_data += [{"_id": str(_id),
                       "deptName": deptName,
                       "parentId": str(parentId),
                       "orderNum": orderNum,
                       "leader_id": str(leader_id),
                       "phone": phone,
                       "roleIds": roleIds,
                       "createTime": createTime,
                       "leader_name": leader_name
                       }]
    return json.jsonify(list_data)


@bp_dept.route('/<enterprise_id>', methods=['POST'])
@jwt_required(optional=False)
def addDepartment(enterprise_id):
    """新增部门"""
    _id = ObjectId()
    dept_info = json.loads(request.get_data().decode("UTF-8"))

    deptName = dept_info.get("deptName")
    parentId = dept_info.get("parentId")
    orderNum = dept_info.get("orderNum")  # string
    leader_id = dept_info.get("leader_id")
    phone = dept_info.get("phone")
    roleIds = dept_info.get("roleIds")
    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    department = Department(_id=_id,
                            deptName=deptName,
                            enterprise_id=enterprise_id,
                            parentId=parentId,
                            orderNum=int(orderNum),
                            leader_id=leader_id,
                            phone=phone,
                            roleIds=roleIds,
                            createTime=createTime)
    department.save()

    return json.jsonify({"_id": str(_id)})


@bp_dept.route('/', methods=['PUT'])
@jwt_required(optional=False)
def updateDepartment():
    """修改部门"""
    dept_info = json.loads(request.get_data().decode("UTF-8"))

    _id = dept_info.get("_id")
    deptName = dept_info.get("deptName")
    parentId = dept_info.get("parentId")
    orderNum = dept_info.get("orderNum")
    leader_id = dept_info.get("leader_id")
    phone = dept_info.get("phone")

    department = Department.objects(_id=_id).first()

    department.update(deptName=deptName)
    department.update(parentId=parentId)
    department.update(orderNum=int(orderNum))
    department.update(leader_id=leader_id)
    department.update(phone=phone)

    return json.jsonify({})


@bp_dept.route('/<dept_id>', methods=['DELETE'])
@jwt_required(optional=False)
def deleteDepartment(dept_id):
    """删除部门"""

    # 删除相关用户对应的部门信息
    users = User.objects(deptId=dept_id)
    for user in users:
        user.deptId = None
        user.save()

    # 删除部门
    Department.objects(_id=dept_id).delete()
    return json.jsonify({})


@bp_dept.route('/<dept_id>', methods=['GET'])
@jwt_required(optional=False)
def getDepartmentInfomation(dept_id):
    """获取部门详细信息"""
    department = Department.objects(_id=dept_id).first()
    deptName = department.deptName
    parentId = department.parentId
    orderNum = department.orderNum
    leader_id = department.leader_id
    phone = department.phone
    roleIds = department.roleIds
    createTime = department.createTime

    return json.jsonify({"_id": dept_id,
                         "deptName": deptName,
                         "parentId": parentId,
                         "orderNum": orderNum,
                         "leader_id": str(leader_id),
                         "phone": phone,
                         "roleIds": roleIds,
                         "createTime": createTime
                         })


@bp_dept.route('/treeselect/<enterprise_id>', methods=['GET'])
@jwt_required(optional=False)
def getDepartmentTree(enterprise_id):
    """获取部门下拉树结构"""
    department_list = Department.objects(enterprise_id=enterprise_id)

    # 构建元素为 {'id':'', 'label':'', 'parent_id':'', 'children':''} 的部门集合
    department_node = []
    for department in department_list:
        department_node += [{'id': str(department._id), 'label': department.deptName,
                             'parent_id': str(department.parentId), 'children': ''}]
    # 获取根节点
    tree = [node for node in department_node if node['parent_id'] == '']  # 不能换成 is None
    # 给每个节点添加子节点
    for node in department_node:
        node['children'] = [n for n in department_node if node['id'] == n['parent_id']]

    # 清除不需要返回的 parent_id
    for node in department_node:
        del node['parent_id']
    # print(tree)

    return json.jsonify(tree)
