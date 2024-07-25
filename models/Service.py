from models.db_models import *
class Service(Base):
    __tablename__="services"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    price=Column(Integer)
    appointments= relationship('Appointment',back_populates='service')
