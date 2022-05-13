from . import db

# 对应数据库中的 user 集合
class User(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 用户id，mongodb自动生成
    email = db.StringField(required=True)  # 用户邮箱
    password = db.StringField(required=True)  # 用户密码
    role = db.StringField(required=True)  # 用户类型：个人或企业
    nickname = db.StringField(default="")  # 用户昵称