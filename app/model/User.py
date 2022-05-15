from . import db

# 对应数据库中的 user 集合
class User(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 用户id，mongodb自动生成
    email = db.StringField(required=True)  # 用户邮箱
    password = db.StringField(required=True)  # 用户密码
    role = db.StringField(required=True)  # 用户类型：个人或企业
    nickname = db.StringField(default="")  # 用户昵称
    phone = db.StringField(default="")  #用户手机号
    gender = db.StringField(default="")  #用户性别：男 女 其他
    dept_id = db.ObjectIdField(default="")  #用户部门ID
    post_id = db.ObjectIdield(default="")  #用户岗位ID
    enterprise_id = db.ObjectIdField(default="")  #用户企业ID