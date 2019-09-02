# coding:utf-8

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect

import redis
import logging
from logging.handlers import RotatingFileHandler


# 数据库
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):

    app = Flask(__name__)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    Session(app)

    CSRFProtect(app)

    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    return app
