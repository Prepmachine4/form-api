from . import db

# 对应数据库中的 user 集合
class Post(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 岗位id，mongodb自动生成
    enterprise_id = db.ObjectIdField(required=True)  #岗位所属企业ID
    postCode = db.StringField(required=True)  # 
    postName = db.StringField(required=True)  # 
    postSort = db.IntField(required=True)  # 
    create_time = db.StringField(required=True)  # 
