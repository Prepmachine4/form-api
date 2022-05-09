from flask import Blueprint, request, json
from bson import ObjectId
from app.models import *
from flask_jwt_extended import jwt_required, get_jwt_identity

bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理定义表单的相关路由
bp_data = Blueprint("data", __name__)  # 创建蓝图，该蓝图管理表单数据的相关路由


@bp_form.route('/<user_id>', methods=['POST'])  # 保存用户表单
@jwt_required(optional=False)
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
                     end_time="",
                     is_template=is_template)
    user_form.save()

    return json.jsonify({"_id": str(user_form._id)})


@bp_form.route('/<form_id>', methods=['DELETE'])  # 删除某一表单
@jwt_required(optional=False)
def deleteForm(form_id):
    # 删除表单结构
    Form.objects(_id=form_id).delete()

    # 删除填写的数据
    FormData.objects(form_id=form_id).delete()
    return json.jsonify({})


@bp_form.route('/<form_id>', methods=['GET'])  # 获取某一表单
@jwt_required(optional=False)
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

    if end_time == "":
        return json.jsonify({"_id": _id, "user_id": user_id, "is_template": is_template,
                             "name": name, "struct": struct, "category": category,
                             "create_time": create_time})
    else:
        return json.jsonify({"_id": _id, "user_id": user_id, "is_template": is_template,
                             "name": name, "struct": struct, "category": category,
                             "create_time": create_time, "setting": {"end_time": end_time}})


@bp_form.route('/forms/<user_id>', methods=['GET'])  # 获取用户的所有表单
@jwt_required(optional=False)
def getUserForms(user_id):
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


@bp_form.route('/setting/<form_id>', methods=['POST'])  # 保存表单设置
@jwt_required(optional=False)
def saveFormSetting(form_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    setting = form_info.get("setting")
    end_time = setting.get("end_time")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time)

    return json.jsonify({})


@bp_form.route('/setting/<form_id>', methods=['GET'])  # 获取表单设置
@jwt_required(optional=False)
def getFormSetting(form_id):
    form = Form.objects(_id=form_id).first()
    end_time = form.end_time

    return json.jsonify({"setting": {"end_time": end_time}})


@bp_form.route('/setting/<form_id>', methods=['PUT'])  # 修改表单设置
@jwt_required(optional=False)
def updateFormSetting(form_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    setting = form_info.get("setting")
    end_time = setting.get("end_time")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time)

    return json.jsonify({})


@bp_form.route('/struct/<form_id>', methods=['GET'])  # 获取表单结构
@jwt_required(optional=False)
def getFormStruct(form_id):
    form_data = Form.objects(_id=form_id).first()
    return json.jsonify(form_data.struct)


@bp_data.route('/<form_id>', methods=['POST'])  # 填写表单
@jwt_required(optional=False)
def fillInForm(form_id):
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    create_time = form_info.get("create_time")
    user_id = form_info.get("user_id")
    data = form_info.get("data")

    form_data = FormData(_id=ObjectId(),
                         create_time=create_time,
                         form_id=form_id,
                         user_id=user_id,
                         data=data)
    form_data.save()

    return json.jsonify({"_id": str(form_data._id)})


@bp_data.route('/forms/<form_id>', methods=['GET'])  # 获取表单所有数据
@jwt_required(optional=False)
def getAllFormInfo(form_id):
    form_data_list = FormData.objects(form_id=form_id)  # 查询 form_data 集合所有匹配 form_id 的项
    list_data = []  # 存放查找内容

    for form_data in form_data_list:
        user_id = form_data.user_id  # type->ObjectId

        user = User.objects(_id=str(user_id)).first()
        user_id = str(user_id)
        email = user.email
        role = user.role

        create_time = form_data.create_time
        data = form_data.data

        list_data += [{"_id": str(form_data._id),
                       "create_time": create_time,
                       "data": data,
                       "user": {"_id": user_id,
                                "email": email,
                                "role": role
                                }
                       }]

    return json.jsonify(list_data)


@bp_data.route('/<user_id>', methods=['GET'])  # 获取某个用户填写的表单
@jwt_required(optional=False)
def getUserForms(user_id):
    form_data_list = FormData.objects(user_id=user_id)  # 查询 form_data 集合所有匹配 user_id 的项
    list_data = []  # 存放查找内容

    for form_data in form_data_list:
        form_id = form_data.form_id  # type->ObjectId
        form = Form.objects(_id=str(form_id)).first()

        # 查询 form_data 集合
        create_time = form_data.create_time
        data = form_data.data
        # 查询 form 集合
        form_id = str(form._id)
        is_template = form.is_template
        name = form.name
        struct = form.struct
        category = form.category
        form_create_time = form.create_time
        end_time = form.end_time
        # 表单创建人
        form_user_id = str(form.user_id)
        # print(form_user_id)
        user = User.objects(_id=form_user_id).first()
        # 查询 user 集合
        email = user.email
        role = user.role

        list_data += [{"_id": str(form_data._id),
                       "create_time": create_time,
                       "data": data,
                       "form": {"_id": form_id,
                                "is_template": is_template,
                                "name": name,
                                "struct": struct,
                                "category": category,
                                "create_time": form_create_time,
                                "setting": {"end_time": end_time},
                                "user": {"_id": form_user_id,
                                         "email": email,
                                         "role": role
                                         }
                                }
                       }]

    return json.jsonify(list_data)
