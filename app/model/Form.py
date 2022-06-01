from cgitb import enable
from email.policy import default
from pickle import TRUE
from random import choices
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
    process_id = db.ObjectIdField(required=False)  # 流程id
    user_range = db.IntField(choices=(0, 1, 2))  # 填写用户类型  0 所有人 1 已注册用户 2 需要秘钥
    password = db.StringField(default="")  # 密钥
    repeat_edit = db.BooleanField(default=False)  # 是否可重复填写
    enable_search = db.BooleanField(default=False)  # 是否全局搜索
    look_result = db.BooleanField(default=False)  # 是否可查看别人填写结果
    look_analysis = db.BooleanField(default=False)  # 是否可查看汇总结果
