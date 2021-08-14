import os

DEBUG = True

DATABASE = {
    'HOST': os.environ.get('DATABASE_HOST'),
    'DB': os.environ.get('DATABASE_NAME'),
    'PORT': os.environ.get('DATABASE_PORT'),
    'USER': os.environ.get('DATABASE_USER'),
    'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
    'TEST_DB': os.environ.get('TEST_DATABASE_NAME'),
}

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(DATABASE["USER"],
                                                                  DATABASE["PASSWORD"],
                                                                  DATABASE["HOST"],
                                                                  DATABASE["PORT"],
                                                                  DATABASE["DB"])

SQLALCHEMY_TEST_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(DATABASE["USER"],
                                                                       DATABASE["PASSWORD"],
                                                                       DATABASE["HOST"],
                                                                       DATABASE["PORT"],
                                                                       DATABASE["TEST_DB"])

SQLALCHEMY_TRACK_MODIFICATIONS = False
