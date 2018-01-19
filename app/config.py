# -*- coding: utf-8 -*-

class Config(object):
    # 密码 string
    SECRET_KEY = 'thefatboy'
    # 服务器名称 string
    HEADER_SERVER = 'SX-KakouRestServer_cs_lm'
    # 加密次数 int
    ROUNDS = 123456
    # token生存周期，默认2小时 int
    EXPIRES = 7200
    # 数据库连接 string
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://123:123@10.123.123.123/Its_Image'
    # 数据库连接 dict
    SQLALCHEMY_BINDS = {}
    # 连接池大小 int
    #SQLALCHEMY_POOL_SIZE = 20
    KKDD_DICT = {
        '1': ('441324601', '永汉'),
        '2': ('441324602', '龙华'),
        '3': ('441324603', '平陵'),
        '4': ('441324604', '鸬鹚'),
        '5': ('441324605', '西埔')
    }
    HPYS_DICT = {
        '1': (2, 'BU', '蓝牌'),
        '2': (1, 'YL', '黄牌'),
        '3': (0, 'WT', '白牌'),
        '4': (3, 'BK', '黑牌'),
        '99': (9, 'QT', '其他')
    }
    FXBH_DICT = {
        '0': (0, '其他'),
        '1': (1, '由东向西'),
        '2': (2, '由西向东'),
        '3': (3, '由南向北'),
        '4': (4, '由北向南'),
        '5': (5, '由东南向西北'),
        '6': (6, '由西北向东南'),
        '7': (8, '由西南向东北'),
        '8': (7, '由东北向西南')
    }


class Develop(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False

