from flask import request, json
from app.model.Form import Form
from flask_jwt_extended import jwt_required
from . import bp_form


@bp_form.route('/setting/<form_id>', methods=['POST'])
@jwt_required(optional=False)
def saveFormSetting(form_id):
    """保存表单设置"""
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    end_time = form_info.get("end_time")
    tags = form_info.get("tags")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time, tags=tags)

    return json.jsonify({})


@bp_form.route('/setting/<form_id>', methods=['GET'])
@jwt_required(optional=False)
def getFormSetting(form_id):
    """获取表单设置"""
    form = Form.objects(_id=form_id).first()
    end_time = form.end_time
    tags = form.tags

    return json.jsonify({"setting": {"end_time": end_time, "tags": tags}})


@bp_form.route('/setting/<form_id>', methods=['PUT'])
#@jwt_required(optional=False)
def updateFormSetting(form_id):
    """修改表单设置"""
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    end_time = form_info.get("end_time")
    tags = form_info.get("tags")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time, tags=tags)

    return json.jsonify({})
