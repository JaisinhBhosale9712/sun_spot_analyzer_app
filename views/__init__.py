from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from views.config import Development
from flask_migrate import Migrate



pymysql.install_as_MySQLdb()
conn = Development.dns_rds
application = Flask(__name__)
application.config["SECRET_KEY"] = Development.secret_key
application.config["SQLALCHEMY_DATABASE_URI"] = conn
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
migrate = Migrate(application, db)
from views import routes
