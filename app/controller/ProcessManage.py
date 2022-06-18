from flask import request, json
from app.model.Process import Process
from app.model.FormData import FormData
from bson import ObjectId
import time
import xmltodict
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_proc

@bp_proc.route('/<enterprise_id>', methods=['POST'])
#@jwt_required(optional=False)
def saveProcess(enterprise_id):
    """保存流程"""
    proc_info = request.get_data()
    proc_info = json.loads(proc_info.decode("UTF-8"))

    svg = proc_info.get("svg")
    xml = proc_info.get("xml")
    name = proc_info.get("name")
    backMethod = proc_info.get("backMethod")
    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    xml_parser = xmltodict.parse(xml,encoding='utf-8')
    xml_json = json.dumps(xml_parser)
    xml_dict = json.loads(xml_json)

    userTaskList = xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask']
    users = []
    if(type(userTaskList) == dict):
        if(userTaskList.get("@userType") == 'assignee'):
            users += [{"type": "assignee", "_id": userTaskList.get("@assignee")}]
        else:
            users += [{"type": "candidateGroups", "_id": userTaskList.get("@candidateGroups")}]
    else:
        for userTask in userTaskList:
            if userTask.get("@userType") == 'assignee':
                users += [{"type": "assignee", "_id": userTask.get("@assignee")}]
            else:
                users += [{"type": "candidateGroups", "_id": userTask.get("@candidateGroups")}]

    proc = Process(_id=ObjectId(),
                   enterprise_id=enterprise_id,
                   svg=svg,
                   xml=xml,
                   name=name,
                   backMethod=backMethod,
                   users=users,
                   createTime=createTime)

    proc.save()

    return json.jsonify({})


@bp_proc.route('/list/<enterprise_id>', methods=['GET'])
#@jwt_required(optional=False)
def getAllProc(enterprise_id):
    """获取流程列表"""
    proc_list = Process.objects(enterprise_id=enterprise_id)
    list_data = []

    for proc in proc_list:
        _id = str(proc._id)
        enterprise_id = str(proc.enterprise_id)
        svg = proc.svg
        xml = proc.xml
        name = proc.name
        backMethod = proc.backMethod
        users = proc.users
        createTime = proc.createTime

        list_data += [{"_id": _id, "enterprise_id": enterprise_id, "svg": svg, "xml": xml,
                       "backMethod":backMethod, "name": name, "users": users, "createTime": createTime}]
    return json.jsonify(list_data)


@bp_proc.route('/<process_id>', methods=['GET'])
#@jwt_required(optional=False)
def getProcInfo(process_id):
    """获取流程详细"""
    proc = Process.objects(_id=process_id).first()

    _id = str(proc._id)
    enterprise_id = str(proc.enterprise_id)
    svg = proc.svg
    xml = proc.xml
    name = proc.name
    backMethod = proc.backMethod
    users = proc.users
    createTime = proc.createTime

    return json.jsonify({"_id": _id, "enterprise_id": enterprise_id, "svg": svg, "xml": xml,
                         "backMethod":backMethod, "name": name, "users": users, "createTime": createTime})


@bp_proc.route('/<process_id>', methods=['DELETE'])
#@jwt_required(optional=False)
def deleteProc(process_id):
    """删除流程"""
    Process.objects(_id=process_id).delete()
    return json.jsonify({})


@bp_proc.route('/<formdata_id>', methods=['PUT'])
#@jwt_required(optional=False)
def abortProc(formdata_id):
    """终止流程"""
    form_data = FormData.objects(_id=formdata_id).first()
    form_data.update(abort=True)
    return json.jsonify({})