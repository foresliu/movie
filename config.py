# coding:utf-8
import redis


class Config(object):
    """配置信息"""
    SECRET_KEY = "cdtaogang**CSDN@uhduqw82981h"

    # 连接mysql数据库
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/movie"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis数据库配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒


class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass

# 构建配置映射关系
config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}