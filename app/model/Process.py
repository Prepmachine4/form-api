from . import db

class Process(db.Document):
    _id = db.ObjectIdField(primary_key=True)    #流程id
    enterprise_id = db.ObjectIdField()  #流程所属的企业id
    svg = db.StringField()  #流程图
    xml = db.StringField()  #流程结构
    name = db.StringField() #流程名
    users = db.ListField()   #流程涉及到的人
    createTime = db.StringField()   #流程创建时间