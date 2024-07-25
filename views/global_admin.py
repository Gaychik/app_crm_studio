from validations import *
from models.init_models import Master,session,Client
from main import *

@app.route('/global_admin/register',methods=['GET'])
def global_admin_view():
     return render_template('/global_admin/register.html')

@app.route("/global_admin/clients")
def global_admin_clients():
    clients=session.query(Client).all()
    return render_template("/global_admin/clients.html", headers=['id','client_name','client_phone','master_name','master_phone'],  clients=clients)
     
@app.route("/global_admin/masters")
def global_admin_masters():
    masters=session.query(Master).all()
    return render_template("/global_admin/masters.html", headers=['id','master_name','master_phone'],  masters=masters)

@app.route("/global_admin/set_master/<int:client_id>", methods=['POST'])
def set_master_to_client(client_id):
     master_info=request.form['select_master']
     master_info=master_info.split(' - ')
     client=session.query(Client).filter_by(id=client_id).first()
     master=session.query(Master).filter_by(name=master_info[0],phone=master_info[1]).first()
     client.master_id=master.id 
     client.master=master 
     session.commit()
     return redirect(url_for('global_admin_clients'))



@app.route('/global_admin/register',methods=['POST'])
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
        return render_template('/global_admin/register.html')