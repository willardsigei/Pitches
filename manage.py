from app import create_app,db
from app.models import User
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand




# Creating app instance

app = create_app('development')