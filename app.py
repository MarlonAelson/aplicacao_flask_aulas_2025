from flask import Flask, render_template, request, flash, redirect
import json
from utils import db
import os
from flask_migrate import Migrate
from models.Usuario import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/primeiro')
def primeiro():
    return render_template('primeiro.html')

@app.route('/segundo')
def segundo():
    return render_template('segundo.html')

@app.route('/terceiro')
def terceiro():
    return render_template('terceiro.html')

@app.route('/quarto')
def quarto():
    return render_template('quarto.html')

@app.route('/parametros')
@app.route('/parametros/<nome>')
def parametros(nome="Usuário Visitante"):
    return render_template('parametros.html', nome=nome.capitalize())

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviarDados', methods=['POST'])
def enviarDados():
    nome = request.form.get('nome')
    return nome

if __name__ == '__main__':
    app.run(debug=True)
