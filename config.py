import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/login'
    SECRET_KEY =os.environ.get('SECRET_KEY')
   
   



config_options = {
'development':DevConfig,
'production':ProdConfig
}