<!-- title: 在线表单处理系统部署说明 -->
# 在线表单处理系统
## api文档
https://www.apifox.cn/apidoc/shared-2bdcb935-e1c5-425a-94f1-fd7bca957868/doc-720236



# 部署说明
## 数据库部署

本项目使用MongoDB数据库，可用docker部署，服务器安装好docker后

```bash
docker pull mongo
docker run -d  --name mongodb -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=[输入数据库密码] mongo
```

## 后端部署

1. 进入form-api目录，该目录为后端代码目录
2. 修改`app/__init__.py`中的数据库配置

```
# 数据库配置
app.config['MONGODB_SETTINGS'] = {
    'db': 'form_system',
    'host': 'localhost',
    'port': 27017,
    'username': 'form',
    'password': 'ldnalKDHlfa@E$das',
    'authentication_source': 'form_system'
}
```

3. 修改uwsgi.ini配置

```
[uwsgi]
socket=127.0.0.1:5000 #本地开启的套接字
wsgi-file = /home/ubuntu/www/form-api/app.py # 后端代码目录
callable = app # 无修修改
```

2. 装好python环境后（可用docker部署）,依次运行

```bash
# 安装python包
pip3 install -r requirements.txt
# 用uwsgi运行服务
uwsgi uwsgi.ini
```



