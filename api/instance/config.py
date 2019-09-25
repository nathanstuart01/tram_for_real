import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Parent Congifuration Class """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_BLACKLIST_ENABLED = os.environ.get('JWT_BLACKLIST_ENABLED')
    JWT_BLACKLIST_TOKEN_CHECKS = os.environ.get('JWT_BLACKLIST_TOKEN_CHECKS')

class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

