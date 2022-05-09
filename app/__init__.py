import flask
from flask import Flask
from app.models import db
from app.formOperation import *
from flask_cors import CORS
from app.login import *
from flask_jwt_extended import JWTManager


def create_app():
    # 创建app
    app = Flask(__name__, static_folder="../static/")
    # 跨域配置
    CORS(app)
    # jwt配置
    app.config["JWT_SECRET_KEY"] = "dsadfasdadsad"
    jwt = JWTManager(app)

    # 静态文件夹的目录 你们不要管
    @app.route('/')
    def get_index():
        return flask.redirect("/static/index.html")

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
    app.register_blueprint(bp_user, url_prefix='/api/user')
    app.register_blueprint(bp_data, url_prefix='/api/data')

    # 注册中间件
    return app
