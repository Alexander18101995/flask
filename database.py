import atexit
from sqlalchemy import Column,String,Integer,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import PG_DSN


engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)

class AdsModel(Base):
    __tablename__ = 'ads_table'

    id = Column(Integer, primary_key=True,autoincrement=True)
    heading = Column(String)
    description = Column(String)
    date_creation = Column(Date)
    owner = Column(String)




Session = sessionmaker(bind=engine)

Base.metadata.create_all()

atexit.register(lambda: engine.dispose())


