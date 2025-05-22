from flask import Flask, render_template, request

app = Flask(__name__)

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
