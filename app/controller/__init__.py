from flask import Blueprint

bp_user = Blueprint("user", __name__)  # 创建蓝图，该蓝图管理用户登录和注册、账户管理相关路由
bp_form = Blueprint("form", __name__)  # 创建蓝图，该蓝图管理表单信息的相关路由
bp_data = Blueprint("data", __name__)  # 创建蓝图，该蓝图管理表单数据的相关路由
bp_role = Blueprint("role", __name__)  # 创建蓝图，该蓝图管理角色的相关路由
bp_post = Blueprint("post", __name__)  # 创建蓝图，该蓝图管理岗位的相关路由
bp_dept = Blueprint("dept", __name__)  # 创建蓝图，该蓝图管理部门的相关路由
bp_sysu = Blueprint("sysu", __name__)  # 创建蓝图，该蓝图管理用户的相关路由
bp_proc = Blueprint("proc", __name__)  # 创建蓝图，该蓝图管理流程的相关路由
bp_audit = Blueprint("audit", __name__)  # 创建蓝图，该蓝图管理审核的相关路由

from . import FormStructManage, FormSettingManage, FormDataManage
from . import RoleManage
from . import UserLogin, UserManage, UserRegister
from . import DepartmentManage
from . import PostManage
from . import ProcessManage
from . import AuditManage
