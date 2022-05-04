from flask_mongoengine import MongoEngine

db = MongoEngine()

# 对应数据库中的user集合
class user(db.Document):
    _id = db.ObjectIdField(primary_key=True)    # 用户id，mongdb自动生成
    email = db.StringField(required=True)   # 用户邮箱
    password = db.StringField(required=True)    # 用户密码
    role = db.StringField(required=True) # 用户角色：个人或企业

# 对应数据库中的form集合
class form(db.Document):
    _id = db.ObjectIdField(primary_key=True)    # 表单id，mongdb自动生成
    user_id = db.ObjectIdField(required=True)    # 设置表单的用户id
    category = db.StringField(required=True)   # 表单类型：问卷型或业务型
    name = db.StringField(required=True)    # 表单名
    struct = db.StringField(required=True) # 表单结构
    status = db.IntField(required=True)  # 表单状态
    create_time = db.StringField(required=True)    #表单的发布时间
    end_time = db.StringField(required=True)   # 表单发布后截止时间
    url = db.StringField() # 表单发布后对应的url

# 对应数据库中的form_data集合
class form_data(db.Document):
    _id = db.ObjectIdField(primary_key=True)    # 表单结果id，mongdb自动生成
    form_id = db.ObjectIdField(required=True)    # 所填写的表单id
    user_id = db.ObjectIdField(required=True)   # 填写该表单的用户id
    result = db.StringField(required=True)  # 表单结果
    status = db.IntField(required=True)   # 表单状态