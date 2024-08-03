from validations import *
from models.init_models import Master,session,Client,Service,Appointment,extract,func,and_
from main import *
import datetime 
import locale
scope_name='/global_admin/'

def get_months():
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    months=[]
    for i in range(1,13):
          months.append(datetime.date(2000,i,1).strftime('%B'))
    return months

@app.route(scope_name)
def global_admin_view():
     locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
     selected_month=request.args.get('selected_month',datetime.datetime.now().strftime('%B'))
     months=get_months()
    #  appointments=session.query(Appointment).filter_by(status="Завершено").all()
     selected_month=datetime.datetime.strptime(selected_month,'%B').month

     result = session.query(    
       Appointment
     ).filter(
          and_(extract('month', Appointment.date) == selected_month,
                Appointment.status =="Завершено")
                ).all() 
     total_price=0
     row_count=0
     for appointment in result:
          if selected_month ==  appointment.date.month:
              row_count+=1
              total_price+=appointment.service.price
     return render_template(scope_name+'financial_analytics.html',months=months,selected_month=selected_month,count=row_count,total=total_price)


@app.route(scope_name+'register_master',methods=['GET'])
def global_admin_register_master_view():
     return render_template(scope_name+'register_master.html')

@app.route(scope_name+'register_service',methods=['GET'])
def global_admin_register_service_view():
     return render_template(scope_name+'register_service.html')

@app.route(scope_name+"clients")
def global_admin_clients():
    clients=session.query(Client).all()
    return render_template(scope_name+"clients.html", headers=['id','client_name','client_phone','master_name','master_phone'],  clients=clients)
     
@app.route(scope_name+"services")
def global_admin_services():
    months=get_months()
    selected_month=request.args.get('selected_month',datetime.datetime.now().strftime('%B'))
    selected_month=datetime.datetime.strptime(selected_month,'%B').month
    query:list[tuple[Service,int]] = (  
    session.query(Service, func.sum(Service.price).label('total_price'))  
    .join(Appointment, Appointment.service_id == Service.id)
    .filter(
          and_(extract('month', Appointment.date) == selected_month,
                Appointment.status =="Завершено")
                )
    .group_by(Service.id)  
    .all()  
)   
    services=[]
    for item in query:
        item[0].revenue_selected_period=item[1]
        services.append(item[0])
         
    
    return render_template(scope_name+"services.html", headers=['id','name','price','revenue for the selected period'],  services=services,months=months,selected_month=selected_month)


@app.route(scope_name+"masters")
def global_admin_masters():
    masters=session.query(Master).all()
    return render_template(scope_name+"masters.html", headers=['id','master_name','master_phone'],  masters=masters)

@app.route(scope_name+"set_master/<int:client_id>", methods=['POST'])
def set_master_to_client(client_id):
     master_info=request.form['select_master']
     master_info=master_info.split(' - ')
     client=session.query(Client).filter_by(id=client_id).first()
     master=session.query(Master).filter_by(name=master_info[0],phone=master_info[1]).first()
     client.master_id=master.id 
     client.master=master 
     session.commit()
     return redirect(url_for('global_admin_clients'))

@app.route(scope_name+"quit_master/<int:master_id>", methods=['GET'])
def quit_master(master_id):
    master=session.query(Master).get(int(master_id))
    if master: 
        session.delete(master)
        session.commit()
    return redirect(url_for('global_admin_masters'))
    
@app.route(scope_name+"quit_service/<int:service_id>", methods=['GET'])
def quit_service(service_id):
    service=session.query(Service).get(int(service_id))
    if service: 
        session.delete(service)
        session.commit()
    return redirect(url_for('global_admin_services'))

@app.route(scope_name+'register_master',methods=['POST'])
def register_master():
        name = request.form['name']
        phone = request.form['phone']
        if validate_name(name):
            master= session.query(Master).filter_by(phone=phone).first()
            if not master:
                master=Master(name=name,phone=phone)
                session.add(master)
                session.commit()
                flash("Регистрация прошла успешно",'success')
            else:
                flash("Такой мастер уже есть!",'info')
        else:
            flash('Регистрация не удалась. Проверьте все поля и повторите попытку', 'danger')
        return render_template(scope_name+'register_master.html')



@app.route(scope_name+'register_service',methods=['POST'])
def register_service():
        name = request.form['name'].rstrip()
        price = request.form['price']
        if validate_name(name):
            service= session.query(Service).filter_by(name=name).first()
            if not service:
                service=Service(name=name,price=price)
                session.add(service)
                session.commit()
                flash("Услуга успешно добавлена",'success')
                
            else:
                flash("Такая услуга уже есть!",'info')
        else:
            flash('Добавить не удалась. Проверьте все поля и повторите попытку', 'danger')
        return render_template(scope_name+'register_service.html')
        