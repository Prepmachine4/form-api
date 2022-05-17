from . import db


# 对应数据库中的 form_data 集合
class FormData(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 表单结果id，mongodb自动生成
    create_time = db.StringField(required=True)  # 表单的发布时间
    form_id = db.ObjectIdField(required=True)  # 所填写的表单id
    user_id = db.ObjectIdField(required=True)  # 填写该表单的用户id
    data = db.StringField(required=True)  # 表单数据
