from sqlalchemy import Column, String, Integer, Float

from utils.db_api.sqlalch_connect import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
