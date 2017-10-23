from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from models.mysql import ConnectDB, MySqlHandle
from models.mysql_config import MYSQL_CONFIG
# from sqlalchemy import Column, String, Integer
from models.models import User

app = Flask(__name__)
# print(my_config)
db_handle = ConnectDB(host=MYSQL_CONFIG.host, user=MYSQL_CONFIG.user, db_name=MYSQL_CONFIG.db_name, password=MYSQL_CONFIG.password, port=MYSQL_CONFIG.port) 
url = db_handle.get_connect()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tigase:qwerqingdao2010@168.235.85.247:3306/to_do_list'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Basemodel = db.Model
# class Test(Basemodel):
	# __tablename__ = 'test'
	# id = Column(Integer, primary_key=True)
	# user_name = Column(String(64))

if __name__ == "__main__":
	table = User()
	table.user_id = "1123"
	table.user_name = "李三"
	table.mobile = "18525006875"
	print(table.mobile, ':', type(table.mobile))
	v_handle = MySqlHandle(session=db.session)
	v_handle.update(table)
	print("add success")



