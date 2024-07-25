from models.db_models import *
from datetime import datetime
class Appointment(Base):
    __tablename__="appointments"
    id=Column(Integer,primary_key=True,autoincrement=True)
    client_id=Column(Integer,ForeignKey('clients.id', ondelete='CASCADE'))
    master_id=Column(Integer,ForeignKey('masters.id', ondelete='CASCADE'))
    service_id=Column(Integer,ForeignKey('services.id', ondelete='CASCADE'))
    date=Column(DateTime, default=datetime.now())
    client=relationship("Client","appointments",primaryjoin="Appointment.client_id == Client.id")
    master=relationship("Master","appointments",primaryjoin="Appointment.master_id == Master.id")
    service=relationship("Service","appointments",primaryjoin="Appointment.service_id == Service.id")

    