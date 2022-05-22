import flask
from flask import Flask
from app.model import db
from app.controller import *
from flask_cors import CORS
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
        'username': 'admin',
        'password': 'ruangongkesheOfmongo',
        'authentication_source': 'admin'
    }
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(bp_form, url_prefix='/api/form')
    app.register_blueprint(bp_user, url_prefix='/api/user')
    app.register_blueprint(bp_data, url_prefix='/api/data')
    app.register_blueprint(bp_role, url_prefix='/api/system/role')
    app.register_blueprint(bp_post, url_prefix='/api/system/post')
    app.register_blueprint(bp_dept, url_prefix='/api/system/dept')
    app.register_blueprint(bp_sysu, url_prefix='/api/system/user')
    app.register_blueprint(bp_proc, url_prefix='/api/process')

    # 注册中间件
    return app
