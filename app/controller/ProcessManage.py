from flask import request, json
from app.model.Process import Process
from bson import ObjectId
import time
import xmltodict
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_proc

@bp_proc.route('/<enterprise_id>', methods=['POST'])
@jwt_required(optional=False)
def saveProcess(enterprise_id):
    """保存流程"""
    proc_info = request.get_data()
    proc_info = json.loads(proc_info.decode("UTF-8"))

    svg = proc_info.get("svg")
    xml = proc_info.get("xml")
    name = proc_info.get("name")
    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    xml_parser = xmltodict.parse(xml,encoding='utf-8')
    xml_json = json.dumps(xml_parser)
    xml_dict = json.loads(xml_json)

    userTaskList = xml_dict['bpmn2:definitions']['bpmn2:process']['bpmn2:userTask']
    users = []
    for userTask in userTaskList:
        users += [{"type":userTask.get("@userType"), "_id":userTask.get("@id")}]

    proc = Process(_id=ObjectId(),
                   enterprise_id=enterprise_id,
                   svg=svg,
                   xml=xml,
                   name=name,
                   users=users,
                   createTime=createTime)

    proc.save()

    return json.jsonify({})


@bp_proc.route('/list/<enterprise_id>', methods=['GET'])
@jwt_required(optional=False)
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
        users = proc.users
        createTime = proc.createTime

        list_data += [{"_id": _id, "enterprise_id": enterprise_id, "svg": svg, "xml": xml,
                       "name": name, "users": users, "createTime": createTime}]
    return json.jsonify(list_data)


@bp_proc.route('/<process_id>', methods=['DELETE'])
@jwt_required(optional=False)
def deleteProc(process_id):
    """获取流程列表"""
    Process.objects(_id=process_id).delete()
    return json.jsonify({})