from flask import Blueprint

bp_user = Blueprint("user", __name__)  # 创建蓝图，该蓝图管理用户登录和注册、账户管理相关路由
bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理表单信息的相关路由
bp_data = Blueprint("data", __name__)  # 创建蓝图，该蓝图管理表单数据的相关路由
bp_role = Blueprint("role", __name__)  # 创建蓝图，该蓝图管理角色的相关路由

from . import FormStructManage,FormSettingManage,FormDataManage
from . import RoleManage
from . import UserLogin,UserManage,UserRegister