from flask import Flask
from app.models import db
from app.formOperation import *

def create_app():
    # 创建app
    app = Flask(__name__)

    # 数据库配置
    app.config['MONGODB_SETTINGS'] = {
        'db': 'form_system',
        'host': '82.157.141.92',
        'port': 27017,
        'connect': True
    }
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(bp_form, url_prefix='/api/form')

    return app