from flask import Blueprint, request, json
from bson import ObjectId
from app.models import *

bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理定义表单的相关路由

@bp_form.route('/<user_id>', methods=['POST'])
def saveForm(user_id):  # 保存用户表单
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    name = form_info.get("name")
    struct = form_info.get("struct")
    category = form_info.get("category")
    status = form_info.get("status")
    create_time = form_info.get("create_time")
    if status == 1:
        end_time = form_info.get("end_time")
    else:
        end_time = ""

    user_form = form(_id=ObjectId(),
                     user_id=user_id,
                     category=category,
                     name=name,
                     struct=struct,
                     status=status,
                     create_time=create_time,
                     end_time=end_time)
    user_form.save()

    return json.jsonify({"_id": str(user_form._id)})

@bp_form.route('/<user_id>/<form_id>', methods=['DELETE'])  #删除用户某一表单
def deleteForm(user_id, form_id):
    form.objects(_id=form_id, user_id=user_id).delete()
    return json.jsonify({})

@bp_form.route('/<form_id>', methods=['GET'])   #获取某一表单
def getForm(form_id):
    form_data = form.objects(_id=form_id).first()

    _id = str(form_data._id)
    user_id = str(form_data.user_id)
    name = form_data.name
    struct = form_data.struct
    category = form_data.category
    status = form_data.status
    create_time = form_data.create_time
    end_time = form_data.end_time

    return json.jsonify({"_id":_id, "user_id":user_id, "name":name,
                         "struct":struct, "category":category, "status":status,
                         "create_time":create_time, "end_time":end_time})


@bp_form.route('/forms/<user_id>', methods=['GET'])   #获取用户的所有表单
def getUserForms(user_id):
    form_data_list = form.objects(user_id=user_id)
    list_data = []

    for form_data in form_data_list:
        _id = str(form_data._id)
        user_id = str(form_data.user_id)
        name = form_data.name
        struct = form_data.struct
        category = form_data.category
        status = form_data.status
        create_time = form_data.create_time
        end_time = form_data.end_time

        list_data += [{"_id":_id, "user_id":user_id, "name":name,
                         "struct":struct, "category":category, "status":status,
                         "create_time":create_time, "end_time":end_time}]

    return json.jsonify(list_data)