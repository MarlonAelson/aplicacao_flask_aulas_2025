from flask import Flask, render_template, request, flash, redirect
import json
from utils import db
import os
from flask_migrate import Migrate
from models.Usuario import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

caminho_db = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.getenv('DB_PATH'))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{caminho_db}"
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
