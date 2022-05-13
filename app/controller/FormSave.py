from flask import request, json
from bson import ObjectId
from app.model import Form
from flask_jwt_extended import jwt_required
from . import bp_form

@bp_form.route('/<user_id>', methods=['POST'])
@jwt_required(optional=False)
def saveForm(user_id):
    '''保存用户表单结构'''
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