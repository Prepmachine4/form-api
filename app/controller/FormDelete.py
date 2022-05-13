from flask import json
from app.model import Form, FormData
from flask_jwt_extended import jwt_required
from . import bp_form

@bp_form.route('/<form_id>', methods=['DELETE'])
@jwt_required(optional=False)
def deleteForm(form_id):
    '''删除某个表单结构'''
    Form.objects(_id=form_id).delete()

    # 删除填写的数据
    FormData.objects(form_id=form_id).delete()
    return json.jsonify({})