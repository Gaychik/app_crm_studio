from models.Client import *
from models.Master import *
from models.Service import *
from models.Appointment import *
from models.Record import *

Base.metadata.create_all(engine)
session.commit()