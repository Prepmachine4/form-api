from email.policy import default
from . import db


# 对应数据库中的 form 集合
class Form(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 表单id，mongodb自动生成
    user_id = db.ObjectIdField(required=True)  # 设置表单的用户id
    category = db.StringField(required=True)  # 表单类型：问卷型或业务型
    name = db.StringField(required=True)  # 表单名
    struct = db.StringField(required=True)  # 表单结构
    create_time = db.StringField(required=True)  # 表单的发布时间
    is_template = db.BooleanField(required=True)  # 表单是否保存为模板
    url = db.StringField()  # 表单发布后对应的url

    # 表单设置
    end_time = db.StringField(default="")  # 表单发布后截止时间
    tags = db.ListField(db.StringField(), default=[])  # 表单标签: 字符串列表
    process_id = db.ObjectIdField(required=False)   # 流程id
