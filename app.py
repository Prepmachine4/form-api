from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
# 数据库配置
app.config['MONGODB_SETTINGS'] = {
    'db': 'form',
    'host': '82.157.141.92',
    'port': 27017
}
db = MongoEngine(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
