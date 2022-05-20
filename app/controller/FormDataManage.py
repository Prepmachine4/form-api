from flask import request, json
from bson import ObjectId
from app.model.Form import Form
from app.model.FormData import FormData
from app.model.User import User
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

    form_data = FormData(_id=ObjectId(),
                         create_time=create_time,
                         form_id=form_id,
                         user_id=user_id,
                         data=data)
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
        deptId = str(user.dept_id)
        postIds = str(user.post_id)
        roleIds = str(user.role_id)

        user_dict = {"_id": user_id, "email": email, "enterprise_id": enterprise_id, "name": name,
                     "nick_name": nick_name, "phone": phone, "deptId": deptId, "postIds": postIds, "roleIds": roleIds}

        # 清除字典中的空项
        for k in list(user_dict.keys()):
            if not user_dict[k]:
                del user_dict[k]

        create_time = form_data.create_time
        data = form_data.data

        list_data += [{"_id": str(form_data._id),
                       "create_time": create_time,
                       "data": data,
                       # "user": {"_id": user_id,
                       #          "email": email,
                       #          "enterprise_id": enterprise_id,
                       #          "name": name,
                       #          "nick_name": nick_name,
                       #          "phone": phone,
                       #          "deptId": deptId,
                       #          "postIds": postIds,
                       #          "roleIds": roleIds
                       #          }
                       "user": user_dict
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
        # 查询 form 集合
        form_id = str(form._id)
        is_template = form.is_template
        form_name = form.name
        struct = form.struct
        category = form.category
        form_create_time = form.create_time
        end_time = form.end_time
        tags = form.tags
        # 表单创建人
        form_user_id = str(form.user_id)

        user = User.objects(_id=form_user_id).first()
        # 查询 user 集合
        email = user.email
        enterprise_id = str(user.enterprise_id)
        user_name = user.name
        nick_name = user.nickname
        phone = user.phone
        deptId = str(user.dept_id)
        postIds = str(user.post_id)
        roleIds = str(user.role_id)

        setting_dict = {"end_time": end_time, "tags": tags}
        user_dict = {"_id": form_user_id, "email": email, "enterprise_id": enterprise_id, "name": user_name,
                     "nick_name": nick_name, "phone": phone, "deptId": deptId, "postIds": postIds, "roleIds": roleIds}

        # 清除字典中的空项
        for k in list(setting_dict.keys()):
            if not setting_dict[k]:
                del setting_dict[k]

        for k in list(user_dict.keys()):
            if not user_dict[k]:
                del user_dict[k]

        if setting_dict:  # 如果字典为空
            list_data += [{"_id": str(form_data._id),
                           "create_time": create_time,
                           "data": data,
                           "form": {"_id": form_id,
                                    "is_template": is_template,
                                    "name": form_name,
                                    "struct": struct,
                                    "category": category,
                                    "create_time": form_create_time,
                                    # "setting": {"end_time": end_time,
                                    #             "tags": tags
                                    #             },
                                    # "user": {"_id": form_user_id,
                                    #          "email": email,
                                    #          "enterprise_id": enterprise_id,
                                    #          "name": user_name,
                                    #          "nick_name": nick_name,
                                    #          "phone": phone,
                                    #          "deptId": deptId,
                                    #          "postIds": postIds,
                                    #          "roleIds": roleIds
                                    #          }
                                    "setting": setting_dict,
                                    "user": user_dict
                                    }
                           }]
        else:
            list_data += [{"_id": str(form_data._id),
                           "create_time": create_time,
                           "data": data,
                           "form": {"_id": form_id,
                                    "is_template": is_template,
                                    "name": form_name,
                                    "struct": struct,
                                    "category": category,
                                    "create_time": form_create_time,
                                    "user": user_dict
                                    }
                           }]

    return json.jsonify(list_data)
