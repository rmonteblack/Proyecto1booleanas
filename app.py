from flask import Flask, render_template, request
from logica import generar_tabla_html

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    expresion = request.form['expresion']
    variables = [v for v in 'pqrstuvwxyz' if v in expresion]
    tabla_html = generar_tabla_html(expresion, variables)
    return render_template('resultado.html', expresion=expresion, tabla_html=tabla_html)

if __name__ == '__main__':
    app.run(debug=True)
