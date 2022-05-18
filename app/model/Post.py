from . import db


# 对应数据库中的 post 集合
class Post(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 岗位id，mongodb自动生成
    enterprise_id = db.ObjectIdField(required=True)  # 岗位所属企业ID
    postCode = db.StringField(required=True)  # 岗位编码
    postName = db.StringField(required=True)  # 岗位名称
    postSort = db.IntField(required=True)  # 显示顺序
    create_time = db.StringField(required=True)  # 创建时间
