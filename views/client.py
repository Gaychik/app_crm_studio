from werkzeug.utils import secure_filename
import os
from math import ceil
from models.init_models import Client,session,Master
from main import *
from validations import *
import re
@app.route("/client/profile/<int:client_id>")
def profile_client(client_id):
    # client = Client.query.get_or_404(client_id)
    client:Client = session.query(Client).get(client_id)
    handler_phone_master=''
    if not client: abort(404) 
    else: 
        if not client.avatar:
           client.avatar="default.png"
        client.appointments=list(client.appointments)
        if client.master:
             handler_phone_master=re.sub(r'\D', '',client.master.phone)
     # Pagination
    per_page = 5
    page = request.args.get('page', 1, type=int)
    role=request.args.get('role','client',type=str)
    masters=[]
    if role!='client':
        masters=session.query(Master).all()

    total_pages = ceil(len(client.appointments) / per_page)
    client.appointments = client.appointments[(page - 1) * per_page:page * per_page]  
    return render_template('/client/profile.html',client=client,total_pages=total_pages,page=page, role=role,masters=masters,handler_phone_master=handler_phone_master)


@app.route('/client/register',methods=['POST'])
def register_client():
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        if validate_name(name) and validate_email(email):
            client= session.query(Client).filter_by(phone=phone).first()
            if not client:
                client=Client(name=name,phone=phone,email=email)
                session.add(client)
                session.commit()
            else:
                flash("Вы уже зарегистрованы!",'info')
        else:
            flash('Регистрация не удалась. Проверьте все поля и повторите попытку', 'danger')
        return render_template('index.html')





@app.route('/upload_avatar/<int:client_id>', methods=['GET', 'POST'])
def upload_avatar(client_id):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
        if file:
            client=session.query(Client).get(client_id)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            client.avatar=filename
            session.commit()
            # Далее сохраните имя файла в базе данных для соответствующего клиента
            # Или обновите имя файла, если он уже существует для клиента   
    return redirect(url_for('profile_client',client_id=client_id))