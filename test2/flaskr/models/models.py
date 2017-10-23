from sqlalchemy import Column, String, Integer, text, DateTime, Text, Date, Time, Numeric, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
# from models.mysql import to_dict


# BaseModel, Model To Dict
def to_dict(self, filter_fields=[]):
    item_dict = {}
    for c in self.__table__.columns:
        if c.name in filter_fields:
            continue
        if isinstance(c.type, DateTime):
            item_dict[c.name] = str(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, Date):
            item_dict[c.name] = str(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, Time):
            item_dict[c.name] = str(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, Numeric):
            item_dict[c.name] = float(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        elif isinstance(c.type, DECIMAL):
            item_dict[c.name] = float(getattr(self, c.name)) if getattr(self, c.name) is not None else None
        else:
            item_dict[c.name] = getattr(self, c.name, None)
    return item_dict
	
BaseModel = declarative_base()
BaseModel.to_dict = to_dict

class User(BaseModel):
    __tablename__ = 'user'

    user_id = Column(String(40), primary_key=True)
    user_name = Column(String(40), nullable=False)
    real_name = Column(String(40))
    mobile = Column(Integer, nullable=False)
    email = Column(String(40))
    birthday = Column(String(40))
    province = Column(String(40))
    city = Column(String(40))
    area = Column(String(200))
    images = Column(String(400))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

class Dream(BaseModel):
    __tablename__ = 'dreams'

    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), nullable=False)
    title = Column(String(400), nullable=False)
    word = Column(Text, nullable=False)
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    remark = Column(String(400))
    created = Column(String(400), nullable=False)
	
class UserPasswordRel(BaseModel):
    __tablename__ = 'user_password_rel'

    id = Column(String(40), primary_key=True)
    user_id = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)