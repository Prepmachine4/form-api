from flask import request, json
from bson import ObjectId
from app.model import FormData
from flask_jwt_extended import jwt_required
from . import bp_data

@bp_data.route('/<form_id>', methods=['POST'])
@jwt_required(optional=False)
def fillInForm(form_id):
    '''填写表单'''
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