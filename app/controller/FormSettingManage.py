from multiprocessing import process
from flask import request, json
from app.model.Form import Form
from flask_jwt_extended import jwt_required
from . import bp_form


@bp_form.route('/setting/<form_id>', methods=['POST'])
#@jwt_required(optional=False)
def saveFormSetting(form_id):
    """保存表单设置"""
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    end_time = form_info.get("end_time")
    tags = form_info.get("tags")
    process_id = form_info.get("process_id")
    user_range = form_info.get("user_range")
    password = form_info.get("password")
    repeat_edit = form_info.get("repeat_edit")
    enable_search = form_info.get("enable_search")
    look_result = form_info.get("look_result")
    look_analysis = form_info.get("look_analysis")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time, tags=tags,process_id=process_id, user_range=user_range,
                password=password, repeat_edit=repeat_edit, enable_search=enable_search,
                look_result=look_result, look_analysis=look_analysis)

    return json.jsonify({})


@bp_form.route('/setting/<form_id>', methods=['GET'])
##@jwt_required(optional=False)
def getFormSetting(form_id):
    """获取表单设置"""
    form = Form.objects(_id=form_id).first()
    end_time = form.end_time
    tags = form.tags
    process_id = form.process_id
    user_range = form.user_range
    password = form.password
    repeat_edit = form.repeat_edit
    enable_search = form.enable_search
    look_result = form.look_result
    look_analysis = form.look_analysis


    return json.jsonify({"setting": {"end_time": end_time, "tags": tags, "process_id":str(process_id),
                        "user_range": user_range, "password":password, "repeat_edit":repeat_edit, 
                        "enable_search":enable_search, "look_result":look_result, "look_analysis":look_analysis}})


@bp_form.route('/setting/<form_id>', methods=['PUT'])
#@jwt_required(optional=False)
def updateFormSetting(form_id):
    """修改表单设置"""
    form_info = request.get_data()
    form_info = json.loads(form_info.decode("UTF-8"))
    end_time = form_info.get("end_time")
    tags = form_info.get("tags")
    process_id = form_info.get("process_id")
    user_range = form_info.get("user_range")
    password = form_info.get("password")
    repeat_edit = form_info.get("repeat_edit")
    enable_search = form_info.get("enable_search")
    look_result = form_info.get("look_result")
    look_analysis = form_info.get("look_analysis")

    form = Form.objects(_id=form_id).first()
    form.update(end_time=end_time, tags=tags,process_id=process_id, user_range=user_range,
                password=password, repeat_edit=repeat_edit, enable_search=enable_search,
                look_result=look_result, look_analysis=look_analysis)

    return json.jsonify({})
