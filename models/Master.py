from models.db_models import *

class Master(Base):
    __tablename__="masters"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    phone=Column(String)
    rate=Column(Integer)
    clients= relationship('Client',back_populates='master')
    appointments= relationship('Appointment',back_populates='master')
    records=relationship('Record',back_populates='master')

