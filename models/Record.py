from models.db_models import *
from datetime import datetime

class Record(Base):
    __tablename__="records"
    id=Column(Integer,primary_key=True,autoincrement=True)
    date=Column(DateTime, default=datetime.now())
    client_id=Column(Integer,ForeignKey('clients.id'))
    master_id=Column(Integer,ForeignKey('masters.id'))
    service_id=Column(Integer,ForeignKey('services.id'))
    client= relationship('Client',back_populates='record')
    master=relationship('Master',back_populates='records')
    service=relationship('Service',back_populates='records')