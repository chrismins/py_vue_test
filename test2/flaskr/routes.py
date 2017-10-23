from main import app
from models import db
from models.mysql import MySqlHandle
from models.models import User

db_handle = MySqlHandle(session=db.session)
rest = db_handle.fetch_list(User)
print(rest)