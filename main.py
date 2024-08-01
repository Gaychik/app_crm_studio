from flask import Flask, render_template, redirect, url_for, request, jsonify,flash,abort
app=Flask(__name__)
app.config['SECRET_KEY'] = 'web_app_crm_studio'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studio.db'
app.config["TEMPLATES_FOLDER"]='/templates'
app.config['UPLOAD_FOLDER']='./static/images/'


if __name__ =='__main__':
    from views.init_views import *
    #Если файл никуда не импортируется , то сервер запускаться будет, иначе не будет
    app.run()