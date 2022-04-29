from flask.json import jsonify
from flask import Blueprint
from app.models import *

bp1 = Blueprint("createForm", __name__)  # 创建蓝图，该蓝图管理定义表单的相关路由

@bp1.route('/')
def createForm():  # put application's code here
    form1 = form(_id=1,
                 user_id=1,
                 category=1,
                 struct=[{"id":1, "type":"single_select", "question":"Who are you?", "choice_num":3, "choice":["ssq","hym","xwt"]},
                         {"id":2, "type":"multi_select", "question":"Who are the team members?", "choice_num":5, "choice":["ssq","hym","xwt","zhq","hrj"]},
                         {"id":3, "type":"fill_blank", "question":"There are __ members and __ leader in the team.", "blank_num":2}],
                 status="未发布",
                 end_time="2023-01-01 00:00:00.000",
                 url="http://www.baidu.com")
    form1.save()
    return jsonify(form.objects)