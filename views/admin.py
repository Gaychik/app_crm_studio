from main import *
from models.init_models import Master,Appointment,Client,session,Record,Service
from validations import *
import math
from datetime import datetime
base_path = '/admin' 
def custom_render(template_name, **kwargs):
     # Базовый путь к шаблонам, который можно изменить
    return render_template(base_path + template_name+'.html', **kwargs)

def get_master(id):
     return session.query(Master).filter_by(id=id).first()
 
@app.route(base_path+"/profile/<int:admin_id>")
def profile_admin(admin_id):
    master=get_master(admin_id)
    return custom_render("/profile",master=master)

@app.route(base_path+"/appointments/<int:admin_id>")
def appointments(admin_id):
    master=get_master(admin_id)
    visits=session.query(Appointment).filter_by(master_id=admin_id).all()
    for appointment in visits:  
            appointment.date = appointment.date.date()  
    per_page = 5
    page = request.args.get('page', 1, type=int)
    total_pages = math.ceil(len(visits) / per_page)
    visits =  visits[(page - 1) * per_page:page * per_page]  
    return custom_render("/appointments",headers=['date','client_name','client_phone','service_name','status'],appointments=visits,master=master,page=page,total_pages=total_pages)



@app.route(base_path+"/clients/<int:admin_id>")
def admin_clients(admin_id):
    master=get_master(admin_id)
    return custom_render("/clients", headers=['id','name','phone','comment'],  master=master)



 

@app.route(base_path+"/record/<int:master_id>/<int:client_id>")
def record(master_id,client_id):
    services=session.query(Service).all()
    master=session.query(Master).filter_by(id=master_id).first()
    client=None
    if client_id>0:
         client=session.query(Client).filter_by(id=client_id).first()
    
    return custom_render("/record",master=master,client=client,services=services)



@app.route(base_path+"/records/<int:admin_id>")
def records(admin_id):
    master=get_master(admin_id)
    per_page = 5
    page = request.args.get('page', 1, type=int)
    total_pages = math.ceil(len(master.records) / per_page)
    master.records =  master.records[(page - 1) * per_page:page * per_page]  
    return custom_render("/records",headers=['client_name','client_phone','date'],master=master,page=page,total_pages=total_pages)



@app.route(base_path+"/complete/<int:record_id>/<status>")
def complete(record_id,status):
      cur_record=session.query(Record).filter_by(id=record_id).first()
      date_obj=datetime.fromisoformat(str(cur_record.date))
      new_appointment=Appointment(client_id=cur_record.client_id,
                                  master_id=cur_record.master_id,
                                  service_id=cur_record.service_id,
                                  date=date_obj.date(),
                                  status=status,
                                  client=cur_record.client,
                                  master=cur_record.master,
                                  service=cur_record.service
                                  )
      session.delete(cur_record)
      session.add(new_appointment)
      session.commit()
      return redirect(url_for('records',admin_id=cur_record.master_id))



    

@app.route(base_path+'/booking/<int:admin_id>',methods=['POST'])
def booking(admin_id):
     name = request.form['name']
     phone = request.form['phone']
     date = request.form['date']
     selected_date = datetime.fromisoformat(date) 
     comment=request.form['comment']
     service_name=request.form['service_name']  #<------
     if validate_name(name):
         master=get_master(admin_id)
         client=session.query(Client).filter_by(phone=phone).first()
         service=session.query(Service).filter_by(name=service_name).first()   #<------
         client.master_id=admin_id
         client.comment=comment
         new_record=Record(date=selected_date,client_id=client.id,master_id=master.id,service_id=service.id)#<------
         session.add(new_record)
         session.commit()
         flash('Запись успешно создана!', 'success')
         return redirect(url_for('profile_admin',admin_id=master.id))
     else:
         flash('Что то пошло не так, попробуйте еще раз!', 'error')
         return redirect(url_for('record',admin_id=admin_id))
         
         
        
         
