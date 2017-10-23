from main import app
from flask_sqlalchemy import SQLAlchemy
from models.mysql import ConnectDB
from models.mysql_config import MYSQL_CONFIG

db_handle = ConnectDB(host=MYSQL_CONFIG.host, user=MYSQL_CONFIG.user, db_name=MYSQL_CONFIG.db_name, password=MYSQL_CONFIG.password, port=MYSQL_CONFIG.port) 
app.config['SQLALCHEMY_DATABASE_URI'] = db_handle.get_connect()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
