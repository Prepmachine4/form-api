from . import db

# 对应数据库中的 role 集合
class Role(db.Document):
    _id = db.ObjectIdField(primary_key=True)  # 角色id，mongodb自动生成
    roleName = db.StringField()  # 角色名
    enterprise_id = db.ObjectIdField()  # 该角色属于的企业
    roleKey = db.StringField()
    roleSort = db.StringField()
    admin = db.BooleanField()   #该角色是否为管理员
    menuTree = db.StringField() #该角色的菜单权限
    createTime = db.StringField()   # 该角色的创建时间
    menuIds = db.StringField()