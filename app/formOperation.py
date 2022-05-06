from flask import Blueprint, request, json
from bson import ObjectId
from app.models import *

bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理定义表单的相关路由
bp_data = Blueprint("data", __name__)  # 创建蓝图，该蓝图管理表单数据的相关路由


@bp_form.route('/<user_id>', methods=['POST'])  # 保存用户表单
def saveForm(user_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    is_template = form_info.get("is_template")
    name = form_info.get("name")
    struct = form_info.get("struct")
    category = form_info.get("category")
    create_time = form_info.get("create_time")

    user_form = Form(_id=ObjectId(),
                     user_id=user_id,
                     category=category,
                     name=name,
                     struct=struct,
                     create_time=create_time,
                     is_template=is_template)
    user_form.save()

    return json.jsonify({"_id": str(user_form._id)})


@bp_form.route('/<form_id>', methods=['DELETE'])  # 删除某一表单
def deleteForm(form_id):
    Form.objects(_id=form_id).delete()
    return json.jsonify({})


@bp_form.route('/<form_id>', methods=['GET'])  # 获取某一表单
def getForm(form_id):
    form_data = Form.objects(_id=form_id).first()

    _id = str(form_data._id)
    user_id = str(form_data.user_id)
    is_template = form_data.is_template
    name = form_data.name
    struct = form_data.struct
    category = form_data.category
    create_time = form_data.create_time
    end_time = form_data.end_time

    return json.jsonify({"_id": _id, "user_id": user_id, "is_template": is_template,
                         "name": name, "struct": struct, "category": category,
                         "create_time": create_time, "end_time": end_time})


@bp_form.route('/forms/<user_id>', methods=['GET'])  # 获取用户的所有表单
def getUserForms(user_id):
    form_data_list = Form.objects(user_id=user_id)
    list_data = []

    for form_data in form_data_list:
        _id = str(form_data._id)
        is_template = form_data.is_template
        name = form_data.name
        struct = form_data.struct
        category = form_data.category
        create_time = form_data.create_time
        end_time = form_data.end_time

        list_data += [{"_id": _id, "user_id": user_id, "name": name,
                       "is_template": is_template, "struct": struct, "category": category,
                       "create_time": create_time, "end_time": end_time}]

    return json.jsonify(list_data)


@bp_form.route('/setting/<form_id>', methods=['POST'])  # 保存表单设置
def saveFormSetting(form_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    end_time = form_info.get("end_time")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time)

    return json.jsonify({})


@bp_form.route('/setting/<form_id>', methods=['GET'])  # 获取表单设置
def getFormSetting(form_id):
    form = Form.objects(_id=form_id).first()
    end_time = form.end_time

    return json.jsonify({"end_time": end_time})


@bp_form.route('/setting/<form_id>', methods=['PUT'])  # 修改表单设置
def updateFormSetting(form_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    end_time = form_info.get("end_time")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time)

    return json.jsonify({})


@bp_data.route('/<form_id>', methods=['POST'])  # 填写表单
def fillInForm(form_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    # form_id = form_info.get("form_id")
    create_time = form_info.get("create_time")
    user_id = form_info.get("user_id")
    result = form_info.get("result")
    status = int(form_info.get("status"))

    form_data = FormData(_id=ObjectId(),
                         create_time=create_time,
                         form_id=form_id,
                         user_id=user_id,
                         result=result,
                         status=status)
    form_data.save()

    return json.jsonify({"_id": str(form_data._id)})


@bp_data.route('/forms/<form_id>', methods=['GET'])  # 获取表单所有数据
def getAllFormInfo(form_id):
    form_data_list = FormData.objects(form_id=form_id)  # 查询 form_data 集合所有匹配 form_id 的项
    list_data = []  # 存放查找内容

    for form_data in form_data_list:
        user_id = form_data.user_id  # type->ObjectId
        user = User.objects(_id=str(user_id)).first()

        create_time = form_data.create_time
        result = form_data.result
        status = form_data.status

        list_data += [{"_id": str(form_data._id),
                       "form_id": str(form_id),
                       "create_time": create_time,
                       "result": result,
                       "status": status,
                       "user": user}]

    return json.jsonify(list_data)
