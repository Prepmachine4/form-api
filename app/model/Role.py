from . import db


# 对应数据库中的 role 集合
class Role(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 角色id，mongodb自动生成
    enterprise_id = db.ObjectIdField()  # 该角色属于的企业
    roleName = db.StringField()  # 角色名
    roleKey = db.StringField()
    roleSort = db.IntField()
    menuIds = db.ListField()
    dataScope = db.StringField()  # 该角色的菜单权限
    createTime = db.StringField()  # 该角色的创建时间
