from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db=SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)


def create_app(config_name):

    app = Flask(__name__)


    # Creating the app configurations
    app.config.from_object(config_options[config_name])