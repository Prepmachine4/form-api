from flask import request, json
import flask
from bson import ObjectId
from app.model.Form import Form
from app.model.FormData import FormData
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_form


@bp_form.route('/forms/list', methods=['GET'])
@jwt_required(optional=False)
def getAllForms():
    """获取全局表单"""
    form_data_list = Form.objects.all()
    list_data = []

    for form_data in form_data_list:
        _id = str(form_data._id)
        user_id = str(form_data.user_id)
        is_template = form_data.is_template
        name = form_data.name
        struct = form_data.struct
        category = form_data.category
        create_time = form_data.create_time
        end_time = form_data.end_time
        tags = form_data.tags

        tmp = {"_id": _id, "user_id": user_id, "is_template": is_template,
               "name": name, "struct": struct, "category": category,
               "create_time": create_time}

        if end_time != "" or len(tags) != 0 or category == "业务型":
            tmp["setting"] = {}
            if end_time != "":
                tmp["setting"]["end_time"] = end_time
            if len(tags) != 0:
                tmp["setting"]["tags"] = tags
            if category == "业务型":
                tmp["setting"]["process_id"] = str(form_data.process_id)
            else:
                tmp["setting"]["user_range"] = form_data.user_range
                tmp["setting"]["password"] = form_data.password
                tmp["setting"]["repeat_edit"] = form_data.repeat_edit
                tmp["setting"]["enable_search"] = form_data.enable_search
                tmp["setting"]["look_result"] = form_data.look_result
                tmp["setting"]["look_Analysis"] = form_data.look_Analysis

        list_data += [tmp]

    return json.jsonify(list_data)


@bp_form.route('/<form_id>', methods=['GET'])
@jwt_required(optional=False)
def getForm(form_id):
    """获取某个表单的信息"""
    form_data = Form.objects(_id=form_id).first()

    _id = str(form_data._id)
    user_id = str(form_data.user_id)
    is_template = form_data.is_template
    name = form_data.name
    struct = form_data.struct
    category = form_data.category
    create_time = form_data.create_time
    end_time = form_data.end_time
    tags = form_data.tags

    tmp = {"_id": _id, "user_id": user_id, "is_template": is_template,
           "name": name, "struct": struct, "category": category,
           "create_time": create_time}

    if end_time != "" or len(tags) != 0 or category == "业务型":
        tmp["setting"] = {}
        if end_time != "":
            tmp["setting"]["end_time"] = end_time
        if len(tags) != 0:
            tmp["setting"]["tags"] = tags
        if category == "业务型":
            tmp["setting"]["process_id"] = str(form_data.process_id)
        else:
            tmp["setting"]["user_range"] = form_data.user_range
            tmp["setting"]["password"] = form_data.password
            tmp["setting"]["repeat_edit"] = form_data.repeat_edit
            tmp["setting"]["enable_search"] = form_data.enable_search
            tmp["setting"]["look_result"] = form_data.look_result
            tmp["setting"]["look_Analysis"] = form_data.look_Analysis

    return json.jsonify(tmp)


@bp_form.route('/forms/<user_id>', methods=['GET'])
@jwt_required(optional=False)
def getUserForms(user_id):
    """获取用户所有表单的信息"""
    #print(get_jwt_identity())  # 获取token里的用户email

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
        tags = form_data.tags

        tmp = {"_id": _id, "user_id": user_id, "is_template": is_template,
               "name": name, "struct": struct, "category": category,
               "create_time": create_time}

        if end_time != "" or len(tags) != 0 or category == "业务型":
            tmp["setting"] = {}
            if end_time != "":
                tmp["setting"]["end_time"] = end_time
            if len(tags) != 0:
                tmp["setting"]["tags"] = tags
            if category == "业务型":
                tmp["setting"]["process_id"] = str(form_data.process_id)
            else:
                tmp["setting"]["user_range"] = form_data.user_range
                tmp["setting"]["password"] = form_data.password
                tmp["setting"]["repeat_edit"] = form_data.repeat_edit
                tmp["setting"]["enable_search"] = form_data.enable_search
                tmp["setting"]["look_result"] = form_data.look_result
                tmp["setting"]["look_Analysis"] = form_data.look_Analysis

        list_data += [tmp]

    return json.jsonify(list_data)


@bp_form.route('/<form_id>', methods=['DELETE'])
@jwt_required(optional=False)
def deleteForm(form_id):
    """删除某个表单结构"""
    Form.objects(_id=form_id).delete()

    # 删除填写的数据
    FormData.objects(form_id=form_id).delete()
    return json.jsonify({})


@bp_form.route('/<user_id>', methods=['POST'])
@jwt_required(optional=False)
def saveForm(user_id):
    """保存用户表单结构"""
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


@bp_form.route('', methods=['PUT'])
@jwt_required(optional=False)
def changeFormStruct():
    '''修改用户表单结构'''
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    _id = form_info.get("_id")
    name = form_info.get("name")
    struct = form_info.get("struct")

    form_data = Form.objects(_id=_id).first()
    form_data.update(name=name, struct=struct)

    return json.jsonify({})


@bp_form.route('/struct/<form_id>', methods=['GET'])
@jwt_required(optional=False)
def getFormStruct(form_id):
    """获取某个表单的结构json"""
    form_data = Form.objects(_id=form_id).first()
    return json.jsonify(form_data.struct)


@bp_form.route('/template/<int:index>', methods=['GET'])
def getFormTemplate(index):
    """获取系统模板"""
    if index == 0:
        return flask.redirect("/static/sys_template/出差审批表.json")
    elif index == 1:
        return flask.redirect("/static/sys_template/设备购买申请表.json")
    elif index == 2:
        return flask.redirect("/static/sys_template/请假申请表.json")
    elif index == 3:
        return flask.redirect("/static/sys_template/意见调查表.json")
    elif index == 4:
        return flask.redirect("/static/sys_template/信息采集表.json")
    else:
        return flask.redirect("/static/sys_template/签到表.json")