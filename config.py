import os

class Config(object):
    SECRET_KEY = '\xacO\xd3\xa4\xf3\x1d\x06\xdf;\x1by\x0f!P\xffi%\xae\x98\xb9'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True