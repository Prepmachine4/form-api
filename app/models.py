from flask_mongoengine import MongoEngine
from datetime import datetime

db = MongoEngine()

# 对应数据库中的user集合
class user(db.Document):
    _id = db.IntField(required=True)    # 用户id
    email = db.StringField(required=True)   # 用户邮箱
    password = db.StringField(required=True)    # 用户密码
    role = db.StringField() # 用户角色：个人或企业

# 对应数据库中的form集合
class form(db.Document):
    _id = db.IntField(required=True)    # 表单id
    user_id = db.IntField(required=True)    # 设置表单的用户id
    category = db.IntField(required=True)   # 表单类型：问卷型(1)或业务型(2)
    struct = db.ListField(required=True) # 表单结构
    status = db.StringField()  # 表单状态
    end_time = db.DateTimeField()   # 表单发布后截止时间
    # end_time = db.DateTimeField(default=datetime.now)
    url = db.URLField() # 表单发布后对应的url

# 对应数据库中的form_data集合
class form_data(db.Document):
    _id = db.IntField(required=True)    # 表单结果id
    form_id = db.IntField(required=True)    # 所填写的表单id
    user_id = db.IntField(required=True)   # 填写该表单的用户id
    result = db.ListField(required=True)  # 表单结果
    status = db.StringField()   # 表单状态