from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tigase:qwerqingdao2010@168.235.85.247:3306/to_do_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class test(db.Model):
	__tablename__ = 'test'
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(64))
	
	def __init__(self,id, user_name):
		self.id = id
		self.user_name = user_name
		
		