# -*- coding: utf-8 -*-
from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from models.mysql import ConnectDB, MySqlHandle
from models.mysql_config import MYSQL_CONFIG
from models.models import User
# import json

app = Flask(__name__)
# print(my_config)
db_handle = ConnectDB(host=MYSQL_CONFIG.host, user=MYSQL_CONFIG.user, db_name=MYSQL_CONFIG.db_name, password=MYSQL_CONFIG.password, port=MYSQL_CONFIG.port) 
url = db_handle.get_connect()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tigase:qwerqingdao2010@168.235.85.247:3306/to_do_list'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

if __name__ == "__main__":
	# table = User()
	# table.user_id = "1126"
	# table.user_name = "刘六"
	# table.mobile = 18625006875
	# table.status = 0
	# table.created = '2017-09-27'
	# print(table.mobile, ':', len(table.mobile))
	v_handle = MySqlHandle(session=db.session)
	# rest = v_handle.fetch_one(User, user_id='1126')
	rest = v_handle.fetch_list(User)
	# print(json.dumps(rest))
	print(rest)



