from . import db

class Audit(db.Document):
    _id = db.ObjectIdField(primary_key=True)    #审批信息的id
    user_id = db.ObjectIdField()  #审批人id
    formdata_id = db.ObjectIdField()    #审批的表单数据id
    index = db.IntField()    #审批顺序
    ip = db.StringField()   #审批ip
    opinion = db.StringField()  #审批意见
    sign = db.StringField() #审批签名
    result = db.BooleanField()   #是否同意
    createTime = db.StringField()   #审批时间