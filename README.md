# 在线表单处理系统
随着在线办公领域的快速发展，很多单位和企业都需要创建、发布、收集、 分析各种业务表单。为了更好地支持表单管理和处理功能，我们开发了一套具有一定通用性和可扩展性的表单处理系统，能够允许用户定义、发布、填写、汇总、 分析、审批各种类型的表单
## api文档
https://www.apifox.cn/apidoc/shared-2bdcb935-e1c5-425a-94f1-fd7bca957868/doc-720236

## 前端项目
https://github.com/Prepmachine4/form-vue

## 设计与亮点
![image](https://user-images.githubusercontent.com/63285063/224487892-c5500ab3-3c7b-4c19-a5c3-3c229e76e962.png)

![image](https://user-images.githubusercontent.com/63285063/224487985-99ecdb8a-0910-449b-ade5-d2f33ab920c7.png)

![image](https://user-images.githubusercontent.com/63285063/224487991-aa51b591-7182-4712-997b-23fb430a9ae0.png)

![image](https://user-images.githubusercontent.com/63285063/224488001-3067c28f-717c-4521-97c0-8b371a485e6e.png)
![image](https://user-images.githubusercontent.com/63285063/224488011-1fbd1537-3b8f-4449-b084-56b5461446f6.png)


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



