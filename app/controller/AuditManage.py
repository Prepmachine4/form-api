from flask import request, json
from app.model.Audit import Audit
from app.model.FormData import FormData
from bson import ObjectId
import time
import xmltodict
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_audit


@bp_audit.route('/<formdata_id>', methods=['POST'])
@jwt_required(optional=False)
def saveAudit(formdata_id):
    """保存审批结果"""
    audit_info = request.get_data()
    audit_info = json.loads(audit_info.decode("UTF-8"))

    user_id = audit_info.get("user_id")
    index = audit_info.get("index")
    opinion = audit_info.get("opinion")
    sign = audit_info.get("sign")
    result = audit_info.get("result")
    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    ip = request.remote_addr

    audit = Audit(_id=ObjectId(),
                  user_id=user_id,
                  formdata_id=formdata_id,
                  index=index,
                  ip=ip,
                  opinion=opinion,
                  sign=sign,
                  result=result,
                  createTime=createTime)

    audit.save()

    # 修改表单数据
    formdata = FormData.objects(_id=formdata_id).first()
    xml = formdata.process_xml
    xml_parser = xmltodict.parse(xml, encoding='utf-8')
    xml_json = json.dumps(xml_parser)
    xml_dict = json.loads(xml_json)

    xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask'][formdata.audit_user_index]["@status"] = "success"
    xml = xmltodict.unparse(xml_dict)
    formdata.update(process_xml=xml)

    userNum = len(xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask'])
    if userNum == formdata.audit_user_index + 1:
        formdata.update(audit_success=True)

    formdata.update(audit_user_index=formdata.audit_user_index + 1)

    return json.jsonify({})
