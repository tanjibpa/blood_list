# default config
import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\xb6\xd5\xdb\x92\xc0\x18\xb1N08>\x7f\xb3\xe4AC\x91\x9a\xec\xfeD\xc20\xe9"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
