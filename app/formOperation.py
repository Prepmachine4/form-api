from flask import Blueprint, request, json
from bson import ObjectId
from app.models import *

bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理定义表单的相关路由


@bp_form.route('/<user_id>', methods=['POST'])
def saveForm(user_id):  # put application's code here
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))

    name = form_info.get("name")
    struct = form_info.get("struct")
    category = form_info.get("category")
    status = form_info.get("status")
    create_time = form_info.get("create_time")
    end_time = form_info.get("end_time")

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


@bp_form.route('/<user_id>/<form_id>', methods=['DELETE'])
def deleteForm(user_id, form_id):
    form.objects(_id=form_id, user_id=user_id).delete()
    return json.jsonify({})
