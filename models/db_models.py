from sqlalchemy import create_engine, Integer, Column, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
#Функция создает подключение к бд и создает обертку над подключением.
engine = create_engine('sqlite:///studio.db', echo=True)
Session = sessionmaker(bind=engine)#Создание сессии
session = Session()#Создание экземпляра сессии

#создаст шаблон для того чтобы с помощью классов создавать таблицы в бд
Base=declarative_base() 

