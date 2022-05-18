from flask import request, json
from bson import ObjectId
from app.model.Post import Post
from app.model.FormData import FormData
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import bp_post
import time


@bp_post.route('/list/<enterprise_id>', methods=['GET'])
@jwt_required(optional=False)
def getPostList(enterprise_id):
    """检查用户权限"""
    if enterprise_id != get_jwt_identity():
        return json.jsonify({}), 401


    """获取公司所有岗位信息"""
    post_list = Post.objects(enterprise_id=enterprise_id)
    list_data = []

    for post in post_list:
        _id = str(post._id)
        postCode = post.enterprise_id
        postName = post.postName
        postSort = post.postSort
        createTime = post.creatTime
        remark = post.remark

        list_data +=[{"_id": _id, "postCode": postCode, "postName": postName, 
                    "postSort": postSort, "createTime": createTime, "remark": remark }]
    
    return json.jsonify(list_data)

@bp_post.route('/<enterprise_id>', methods=['POST'])
@jwt_required(optional=False)
def savePost(enterprise_id):
    """检查用户权限"""
    if enterprise_id != get_jwt_identity():
        return json.jsonify({}), 401
    
    """新增岗位信息"""
    post_info = request.get_data()
    post_info = json.loads(post_info.decode("UTF-8"))


    createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    postCode = post_info.get("postCode")
    postName = post_info.get("postName")
    postSort = post_info.get("postSort")
    remark = post_info.get("remark") if "remark" in post_info.keys() else ""

    post = Post(_id=ObjectId(),
                         enterprise_id=enterprise_id,
                         postCode=postCode,
                         postName=postName,
                         postSort=postSort,
                         createTime=createTime,
                         remark=remark)
    post.save()

    return json.jsonify({"_id": str(post._id)})