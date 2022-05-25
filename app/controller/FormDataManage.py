from flask import request, json
from bson import ObjectId
from app.model.Form import Form
from app.model.FormData import FormData
from app.model.User import User
from app.model.Audit import Audit
from app.model.Department import Department
from app.model.Process import Process
from flask_jwt_extended import jwt_required
from . import bp_data


@bp_data.route('/<form_id>', methods=['POST'])
@jwt_required(optional=False)
def fillInForm(form_id):
    """填写表单"""
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    create_time = form_info.get("create_time")
    user_id = form_info.get("user_id")
    data = form_info.get("data")
    process_id = Form.objects(_id=str(form_id)).first().process_id
    process_xml = Process.objects(_id=str(process_id)).first().xml
    audit_user_index = 0
    audit_success = False

    form_data = FormData(_id=ObjectId(),
                         create_time=create_time,
                         form_id=form_id,
                         user_id=user_id,
                         data=data,
                         process_xml=process_xml,
                         audit_user_index=audit_user_index,
                         audit_success=audit_success)
    form_data.save()



    return json.jsonify({"_id": str(form_data._id)})


@bp_data.route('/forms/<form_id>', methods=['GET'])
@jwt_required(optional=False)
def getAllFormData(form_id):
    """获取表单所有数据"""
    form_data_list = FormData.objects(form_id=form_id)  # 查询 form_data 集合所有匹配 form_id 的项
    list_data = []  # 存放查找内容

    for form_data in form_data_list:
        user_id = form_data.user_id  # type->ObjectId

        user = User.objects(_id=str(user_id)).first()
        user_id = str(user_id)
        email = user.email
        enterprise_id = str(user.enterprise_id)
        name = user.name
        nick_name = user.nickname
        phone = user.phone
        deptName = Department.objects(_id=str(user.deptId)).first().deptName

        user_dict = {"_id": user_id, "email": email, "enterprise_id": enterprise_id, "name": name,
                     "nick_name": nick_name, "phone": phone, "deptName": deptName}

        # # 清除字典中的空项
        # for k in list(user_dict.keys()):
        #     if not user_dict[k]:
        #         del user_dict[k]

        create_time = form_data.create_time
        data = form_data.data

        process_xml = form_data.process_xml
        audit_user_index = form_data.audit_user_index
        audit_success = form_data.audit_success

        audit_list = Audit.objects(formdata_id=str(form_data._id))
        audit_list_data = []
        for audit in audit_list:
            audit_id = str(audit._id)
            audit_user_id = str(audit.user_id)
            audit_formdata_id = str(audit.formdata_id)
            audit_index = audit.index
            audit_ip = audit.ip
            audit_opinion = audit.opinion
            audit_sign = audit.sign
            audit_result = audit.result
            audit_createTime = audit.createTime
            audit_user_name = User.objects(_id=audit_user_id).first().name

            audit_list_data += [{
                "_id": audit_id,
                "user_id": audit_user_id,
                "formdata_id": audit_formdata_id,
                "index": audit_index,
                "ip": audit_ip,
                "opinion": audit_opinion,
                "sign": audit_sign,
                "result": audit_result,
                "createTime": audit_createTime,
                "user_name": audit_user_name
            }]

        list_data += [{"_id": str(form_data._id),
                       "create_time": create_time,
                       "data": data,
                       "process_xml": process_xml,
                       "audit_user_index": audit_user_index,
                       "audit_success": audit_success,
                       "user": user_dict,
                       "audit_history": audit_list_data
                       }]

    return json.jsonify(list_data)


@bp_data.route('/<user_id>', methods=['GET'])
@jwt_required(optional=False)
def getUserForms(user_id):
    """获取某个用户填写的表单"""
    form_data_list = FormData.objects(user_id=user_id)  # 查询 form_data 集合所有匹配 user_id 的项
    list_data = []  # 存放查找内容

    for form_data in form_data_list:
        form_id = form_data.form_id  # type->ObjectId
        form = Form.objects(_id=str(form_id)).first()

        # 查询 form_data 集合
        create_time = form_data.create_time
        data = form_data.data
        process_xml = form_data.process_xml
        audit_user_index = form_data.audit_user_index
        audit_success = form_data.audit_success

        # 查询 form 集合
        form_id = str(form._id)
        is_template = form.is_template
        form_name = form.name
        struct = form.struct
        category = form.category
        form_create_time = form.create_time

        # settings
        end_time = form.end_time
        tags = form.tags
        process_id = str(form.process_id)

        # 表单创建人
        form_user_id = str(form.user_id)

        user = User.objects(_id=form_user_id).first()
        # 查询 user 集合
        email = user.email
        enterprise_id = str(user.enterprise_id)
        user_name = user.name
        nick_name = user.nickname
        phone = user.phone

        # 查询 audit 集合
        audit_list = Audit.objects(formdata_id=str(form_data._id))
        audit_list_data = []
        for audit in audit_list:
            audit_id = str(audit._id)
            audit_user_id = str(audit.user_id)
            audit_formdata_id = str(audit.formdata_id)
            audit_index = audit.index
            audit_ip = audit.ip
            audit_opinion = audit.opinion
            audit_sign = audit.sign
            audit_result = audit.result
            audit_createTime = audit.createTime

            audit_user_name = User.objects(_id=audit_user_id).first().name

            audit_list_data += [{
                "_id": audit_id,
                "user_id": audit_user_id,
                "formdata_id": audit_formdata_id,
                "index": audit_index,
                "ip": audit_ip,
                "opinion": audit_opinion,
                "sign": audit_sign,
                "result": audit_result,
                "createTime": audit_createTime,
                "user_name": audit_user_name
            }]

        setting_dict = {"end_time": end_time, "tags": tags, "process_id": process_id}
        user_dict = {"_id": form_user_id, "email": email, "enterprise_id": enterprise_id, "name": user_name,
                     "nick_name": nick_name, "phone": phone}

        list_data += [{"_id": str(form_data._id),
                       "create_time": create_time,
                       "data": data,
                       "process_xml": process_xml,
                       "audit_user_index": audit_user_index,
                       "audit_success": audit_success,
                       "form": {"_id": form_id,
                                "is_template": is_template,
                                "name": form_name,
                                "struct": struct,
                                "category": category,
                                "create_time": form_create_time,
                                "setting": setting_dict,
                                "user": user_dict
                                },
                       "audit_history": audit_list_data
                       }]

    return json.jsonify(list_data)
