from sqlalchemy.orm import sessionmaker
from utils.db_api.sqlalch_connect import engine

Session = sessionmaker(bind=engine)
