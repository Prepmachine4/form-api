from flask_mongoengine import MongoEngine

db = MongoEngine()


# 对应数据库中的 user 集合
class User(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 用户id，mongodb自动生成
    email = db.StringField(required=True)  # 用户邮箱
    password = db.StringField(required=True)  # 用户密码
    role = db.StringField(required=True)  # 用户类型：个人或企业
    nickname = db.StringField(default="")


# 对应数据库中的 form 集合
class Form(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 表单id，mongodb自动生成
    user_id = db.ObjectIdField(required=True)  # 设置表单的用户id
    category = db.StringField(required=True)  # 表单类型：问卷型或业务型
    name = db.StringField(required=True)  # 表单名
    struct = db.StringField(required=True)  # 表单结构
    create_time = db.StringField(required=True)  # 表单的发布时间
    end_time = db.StringField(default="")  # 表单发布后截止时间
    is_template = db.BooleanField(required=True)  # 表单是否保存为模板
    url = db.StringField()  # 表单发布后对应的url


# 对应数据库中的 form_data 集合
class FormData(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 表单结果id，mongodb自动生成
    create_time = db.StringField(required=True)  # 表单的发布时间
    form_id = db.ObjectIdField(required=True)  # 所填写的表单id
    user_id = db.ObjectIdField(required=True)  # 填写该表单的用户id
    data = db.StringField(required=True)  # 表单数据
