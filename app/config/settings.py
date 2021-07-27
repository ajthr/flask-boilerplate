import os

DEBUG = True

DATABASE = {
    'HOST': os.environ.get('DATABASE_HOST'),
    'NAME': os.environ.get('DATABASE_NAME'),
    'PORT': os.environ.get('DATABASE_PORT'),
    'USER': os.environ.get('DATABASE_USER'),
    'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
}

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(DATABASE["USER"],
                                                                  DATABASE["PASSWORD"],
                                                                  DATABASE["HOST"],
                                                                  DATABASE["PORT"],
                                                                  DATABASE["NAME"])
SQLALCHEMY_TRACK_MODIFICATIONS = False
