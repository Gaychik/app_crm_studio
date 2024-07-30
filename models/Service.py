from models.db_models import *
class Service(Base):
    __tablename__="services"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    price=Column(Integer)
    revenue_selected_period=Column(Integer,default=0)
    records=relationship('Record',back_populates='service')
    
