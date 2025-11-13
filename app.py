from flask import Flask, render_template, request
from logica import generar_tabla_html

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    expresion = request.form['expresion']
    # Esta línea encuentra las variables automáticamente
    variables = sorted(list(set(v for v in 'pqrstuvwxyz' if v in expresion)))
    tabla_html = generar_tabla_html(expresion, variables)
    return render_template('resultado.html', expresion=expresion, tabla_html=tabla_html)

# --- AÑADE ESTA NUEVA RUTA ---
@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')
# -------------------------------

if __name__ == '__main__':
    app.run(debug=True)