from models.db_models import *
from datetime import datetime
class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id', ondelete='CASCADE'))
    master_id = Column(Integer, ForeignKey('masters.id', ondelete='CASCADE'))
    service_id = Column(Integer, ForeignKey('services.id', ondelete='CASCADE'))
    date = Column(DateTime, default=datetime.now)
    
    client = relationship("Client", backref="appointments")
    master = relationship("Master", backref="appointments")
    service = relationship("Service", backref="appointments")

    