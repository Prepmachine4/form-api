from . import db


# 对应数据库中的 user 集合
class User(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 用户id，mongodb自动生成
    email = db.StringField(required=True)  # 用户邮箱
    password = db.StringField(required=True)  # 用户密码
    role = db.StringField(required=True)  # 用户类型：个人或企业
    nickname = db.StringField(default="")  # 用户昵称
    phone = db.StringField(default="")  # 用户手机号
    name = db.StringField(default="")  # 真实姓名

    # 以下为企业用户专有
    deptId = db.ObjectIdField()  # 用户部门ID
    enterprise_id = db.ObjectIdField()  # 用户企业ID
    roleIds = db.ListField()  # 用户角色ID列表
    postIds = db.ListField()  # 用户岗位ID列表
