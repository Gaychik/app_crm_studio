from validations import *
from models.init_models import Master,session,Client,Service
from main import *
scope_name='/global_admin/'
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
    services=session.query(Service).all()
    return render_template(scope_name+"services.html", headers=['id','name','price','revenue for the selected period'],  services=services)


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
        name = request.form['name']
        price = request.form['price']
        if validate_name(name):
            service= session.query(Service).filter_by(name=name).first()
            if not service:
                serivce=Service(name=name,price=price)
                session.add(serivce)
                session.commit()
                flash("Услуга успешно добавлена",'success')
                
            else:
                flash("Такая услуга уже есть!",'info')
        else:
            flash('Добавить не удалась. Проверьте все поля и повторите попытку', 'danger')
        return render_template(scope_name+'register_service.html')
        