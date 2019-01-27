import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Parent Congifuration Class """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

