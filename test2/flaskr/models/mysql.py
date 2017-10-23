import json

class ConnectDB(object):
	def __init__(self, **kwargs):
		self.host = kwargs.get('host')
		self.user = kwargs.get('user')
		self.password = kwargs.get('password')
		self.db_name = kwargs.get('db_name')
		self.port = kwargs.get('port')

	def get_connect(self):
		connection = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'
		connection = connection.format(self.user, self.password, self.host, self.port, self.db_name)
		# connection = 'mysql+pymysql://%s:%s@%s:%d/%s' % (self.user, self.password, self.host,self.port,self.db_name)
		return connection
		
		
class MySqlHandle(object):
	def __init__(self, **kwargs):
		super(MySqlHandle, self).__init__()
		self.session = kwargs.get('session')
		
	def add(self, entry):
		try:
			self.session.add(entry)
			self.session.commit()
		except Exception as ex:
			raise ex
		
	def update(self, entry):
		try:
			self.session.merge(entry)
			self.session.commit()
		except Exception as ex:
			raise ex
			
	def delete(self, entry):
		try:
			self.session.delete(entry)
			self.session.commit()
		except Exception as ex:
			raise ex
			
	def fetch_one(self, entry, **kwargs):
		try:
			results = self.session.query(entry).filter_by(**kwargs).first()
			rest = results.to_dict()
			return json.dumps(rest)
		except Exception as ex:
			raise ex
			
	def fetch_list(self, entry, **kwargs):
		try:
			results = self.session.query(entry).filter_by(**kwargs).all()
			results = [json.dumps(item.to_dict()) for item in results]
			return results
		except Exception as ex:
			raise ex
		