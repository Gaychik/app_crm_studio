from models.db_models import *

#Base это класс(шаблон) от корого наследуются другие классы.
#Это класс содержит различные функции и свойства, 
# которые помогают наследникам позже превратиться в таблицу в базе данных
class Client(Base):
    __tablename__='clients'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    email=Column(String,nullable=True)
    phone=Column(String)
    avatar=Column(String,nullable=True)
    comment=Column(String,nullable=True)
    master_id=Column(Integer,ForeignKey('masters.id', ondelete='SET NULL'))
    master= relationship('Master',back_populates='clients')
    appointments= relationship('Appointment',back_populates='client')
    record = relationship('Record',back_populates='client')




