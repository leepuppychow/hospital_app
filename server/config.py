import os

class Config:
  DEBUG = False
  DEVELOPMENT = False
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
  pass


class StageConfig(Config):
  DEBUG = True


class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True