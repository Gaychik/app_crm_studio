from validations import *
from models.init_models import Client,Master,session
from main import *
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    phone = request.form['phone']
    # Логика входа пользователя  или мастера(например, проверка в базе данных)
    client=session.query(Client).filter_by(phone=phone).first()
    master=session.query(Master).filter_by(phone=phone).first()
    if client:
        return redirect(url_for('profile_client',client_id=client.id)) 
    elif master:
        return redirect(url_for('profile_admin',admin_id=master.id))
    flash('Не найден телефон, повторите попытку либо пройдите регистрацию', 'danger')
    return render_template('index.html')


