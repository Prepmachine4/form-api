from flask import json
from app.model import Form
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_form

@bp_form.route('/<form_id>', methods=['GET'])
@jwt_required(optional=False)
def getForm(form_id):
    '''获取某个表单的信息'''
    form_data = Form.objects(_id=form_id).first()

    _id = str(form_data._id)
    user_id = str(form_data.user_id)
    is_template = form_data.is_template
    name = form_data.name
    struct = form_data.struct
    category = form_data.category
    create_time = form_data.create_time
    end_time = form_data.end_time

    if end_time == "":
        return json.jsonify({"_id": _id, "user_id": user_id, "is_template": is_template,
                             "name": name, "struct": struct, "category": category,
                             "create_time": create_time})
    else:
        return json.jsonify({"_id": _id, "user_id": user_id, "is_template": is_template,
                             "name": name, "struct": struct, "category": category,
                             "create_time": create_time, "setting": {"end_time": end_time}})


@bp_form.route('/forms/<user_id>', methods=['GET'])
@jwt_required(optional=False)
def getUserForms(user_id):
    '''获取用户所有表单的信息'''
    print(get_jwt_identity())  # 获取token里的用户email

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

        if end_time == "":
            list_data += [{"_id": _id, "user_id": user_id, "name": name,
                           "is_template": is_template, "struct": struct, "category": category,
                           "create_time": create_time}]
        else:
            list_data += [{"_id": _id, "user_id": user_id, "name": name,
                           "is_template": is_template, "struct": struct, "category": category,
                           "create_time": create_time, "setting": {"end_time": end_time}}]

    return json.jsonify(list_data)


@bp_form.route('/struct/<form_id>', methods=['GET'])
def getFormStruct(form_id):
    '''获取某个表单的结构json'''
    form_data = Form.objects(_id=form_id).first()
    return json.jsonify(form_data.struct)