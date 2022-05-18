from flask import request, json
from bson import ObjectId
from app.model.Post import Post
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
        postCode = post.postCode
        postName = post.postName
        postSort = post.postSort
        createTime = post.createTime
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
    
    print(1)
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

@bp_post.route('', methods=['PUT'])
@jwt_required(optional=False)
def updatePost():

    """修改岗位信息"""
    post_info = request.get_data()
    post_info = json.loads(post_info.decode("UTF-8"))


    _id = post_info.get("_id")
    postCode = post_info.get("postCode")
    postName = post_info.get("postName")
    postSort = post_info.get("postSort")
    remark = post_info.get("remark") if "remark" in post_info.keys() else ""

    """检查用户权限"""
    post = Post.objects(_id=_id).first()
    enterprise_id = post.enterprise_id
    if enterprise_id != get_jwt_identity():
        return json.jsonify({}), 401

    post.update(postCode=postCode,
                postName=postName,
                postSort=postSort,
                remark=remark)

    return json.jsonify({"_id": str(post._id)})

@bp_post.route('/<post_id>', methods=['DELETE'])
@jwt_required(optional=False)
def deletePost(post_id):

    """检查用户权限"""
    post = Post.objects(_id=post_id).first()
    enterprise_id = str(post.enterprise_id)
    if enterprise_id != get_jwt_identity():
        return json.jsonify({}), 401
    
    """删除岗位信息"""
    post = Post.objects(_id=post_id).delete()

    return json.jsonify({})    

@bp_post.route('/<post_id>', methods=['GET'])
@jwt_required(optional=False)
def getPost(post_id):
    """检查用户权限"""
    post = Post.objects(_id=post_id).first()
    enterprise_id = str(post.enterprise_id)
    if enterprise_id != get_jwt_identity():
        return json.jsonify({}), 401
    

    """获取岗位详细信息"""
    postCode = post.postCode
    postName = post.postName
    postSort = post.postSort
    createTime = post.createTime
    remark = post.remark


    return json.jsonify({"_id": post_id, "postCode": postCode, "postName": postName, 
                "postSort": postSort, "createTime": createTime, "remark": remark })