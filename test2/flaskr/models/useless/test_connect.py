from models.mysql import ConnectDB
from models.mysql_config import MYSQL_CONFIG

db_handle = ConnectDB(host=MYSQL_CONFIG.host, user=MYSQL_CONFIG.user, db_name=MYSQL_CONFIG.db_name, password=MYSQL_CONFIG.password, port=MYSQL_CONFIG.port)
result = db_handle.get_connect()

print(result)