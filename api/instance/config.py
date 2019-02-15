import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Parent Congifuration Class """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:password@db:5432/tram'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ilovesnow'
    JWT_SECRET_KEY= os.environ.get('JWT_SECRET_KEY') or 'ilovecarpooling'

class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

