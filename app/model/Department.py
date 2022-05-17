from . import db


# 对应数据的 department 集合
class Department(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 部门id，mongodb自动生成
    deptName = db.StringField(required=True)  # 部门名称
    enterprise_id = db.ObjectIdField(required=True)  # 所属企业id
    parentId = db.StringField(required=True)  # 父节点id
    orderNum = db.IntField(required=True)  # 订单数量
    leader_id = db.ObjectIdField(required=True)  # 负责人id
    phone = db.StringField(required=True)  # 部门电话
    createTime = db.StringField(required=True)  # 创建时间
