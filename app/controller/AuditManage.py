from concurrent.futures import process
from flask import request, json
from app.model.Audit import Audit
from app.model.FormData import FormData
from app.model.Form import Form
from app.model.User import User
from app.model.Department import Department
from app.model.Process import Process
from bson import ObjectId
import time
import xmltodict
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_audit


@bp_audit.route('/<formdata_id>', methods=['POST'])
#@jwt_required(optional=False)
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

    form_id = formdata.form_id
    process_id = Form.objects(_id=form_id).first().process_id
    backMethod = Process.objects(_id=process_id).first().backMethod  # 是否回退到第一步

    if result == True:
        xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask'][formdata.audit_user_index][
            "@status"] = "success"
        xml = xmltodict.unparse(xml_dict)
        formdata.update(process_xml=xml)

        userNum = len(xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask'])
        if userNum == formdata.audit_user_index + 1:
            formdata.update(audit_success=True)

        formdata.update(audit_user_index=formdata.audit_user_index + 1)
    else:
        if backMethod == 0:  # 回退一步
            xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask'][formdata.audit_user_index][
                "@status"] = "reject"
            xml = xmltodict.unparse(xml_dict)
        else:  # 回退到从头开始
            for i in range(formdata.audit_user_index + 1):
                xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask'][i]["@status"] = "reject"
            xml = xmltodict.unparse(xml_dict)
            formdata.update(audit_user_index=0)

        formdata.update(process_xml=xml)

    return json.jsonify({})


@bp_audit.route('/list/now/<user_id>', methods=['GET'])
#@jwt_required(optional=False)
def getNowAudit(user_id):
    """获取用户当前需要进行的审批"""
    formData_list = FormData.objects(audit_success=False, abort=False)
    postIds = User.objects(_id=user_id).first().postIds
    data_list = []

    for formdata in formData_list:
        audit_user_index = formdata.audit_user_index
        process_xml = formdata.process_xml
        if process_xml == "":
            continue
        form_id = formdata.form_id
        form = Form.objects(_id=form_id).first()
        if form == None:
            continue
        process_id = form.process_id
        process = Process.objects(_id=process_id).first()
        if process == None:
            continue
        users = process.users
        audit_user = users[audit_user_index]
        print(audit_user)
        if (audit_user["type"] == "assignee" and audit_user["_id"] == user_id) \
                or (audit_user["type"] == "candidateGroups" and audit_user["_id"] in postIds):
            formdata_id = formdata._id
            create_time = formdata.create_time
            data = formdata.data
            process_xml = str(formdata.process_xml)
            audit_user_index = formdata.audit_user_index
            audit_success = formdata.audit_success

            form = Form.objects(_id=form_id).first()
            if form == None:
                continue
            form_name = form.name
            form_struct = form.struct

            data_user_id = formdata.user_id
            user = User.objects(_id=data_user_id).first()
            if user == None:
                continue
            user_email = user.email
            user_name = user.name
            user_nick_name = user.nickname
            user_phone = user.phone
            user_deptId = user.deptId
            user_dept = Department.objects(_id=user_deptId).first()
            if user_dept == None:
                continue
            user_deptName = user_dept.deptName

            data = {"_id": str(formdata_id), "create_time": create_time, "data": data, "process_xml": process_xml,
                    "audit_user_index": audit_user_index, "audit_success": audit_success,
                    "form": {"_id": str(form_id), "name": form_name, "struct": form_struct}}
            data_user = {"_id": str(data_user_id), "email": user_email, "deptName": user_deptName}
            if user_name != "":
                data_user["name"] = user_name
            if user_nick_name != "":
                data_user["nick_name"] = user_nick_name
            if user_phone != "":
                data_user["phone"] = user_phone
            data["user"] = data_user

            data_list += [data]

    return json.jsonify(data_list)


@bp_audit.route('/list/history/<user_id>', methods=['GET'])
#@jwt_required(optional=False)
def getHistoryAudit(user_id):
    """获取审批历史"""
    audit_list = Audit.objects(user_id=user_id)
    data_list = []
    for audit in audit_list:
        formdata_id = audit.formdata_id
        formdata = FormData.objects(_id=formdata_id).first()
        if formdata == None:
            continue
        create_time = formdata.create_time
        data = formdata.data
        process_xml = str(formdata.process_xml)
        audit_user_index = int(formdata.audit_user_index)
        audit_success = formdata.audit_success

        form_id = formdata.form_id
        form = Form.objects(_id=form_id).first()
        if form == None:
            continue
        form_name = form.name
        form_struct = form.struct

        form_user_id = formdata.user_id
        user = User.objects(_id=form_user_id).first()
        if user == None:
            continue
        user_email = user.email
        user_name = user.name
        user_nick_name = user.nickname
        user_phone = user.phone
        user_deptId = user.deptId
        user_dept = Department.objects(_id=user_deptId).first()
        if user_dept == None:
            continue        
        user_deptName = user_dept.deptName

        data = {"_id": str(formdata_id), "create_time": create_time, "data": data, "process_xml": process_xml,
                "audit_user_index": audit_user_index, "audit_success": audit_success,
                "form": {"_id": str(form_id), "name": form_name, "struct": form_struct}}
        data_user = {"_id": str(form_user_id), "email": user_email, "deptName": user_deptName}
        if user_name != "":
            data_user["name"] = user_name
        if user_nick_name != "":
            data_user["nick_name"] = user_nick_name
        if user_phone != "":
            data_user["phone"] = user_phone
        data["user"] = data_user

        data_list += [data]

    return json.jsonify(data_list)
