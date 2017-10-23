from mysql import ConnectDB
from flask_sqlalchemy import SQLAlchemy

class db_handle(ConnectDB):
	def __init__(self, ConnectDB, **kwargs):
		self.url = ConnectDB(**kwargs).
		db = SQLAlchemy()
		self.session = db.session