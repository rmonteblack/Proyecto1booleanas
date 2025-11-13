import itertools
import re

def parentesis_balanceados(expresion):
    stack = []
    for char in expresion:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def evaluar(expresion, valores):
    expr = expresion

    # 1. Reemplazamos los operadores lógicos ANTES de poner los valores
    expr = expr.replace("<->", "==")
    expr = expr.replace("->", "<=")  # <-- ¡ESTE ES EL CAMBIO PRINCIPAL!
    expr = expr.replace("^", " and ") # Asumiendo que ^ es AND
    expr = expr.replace("||", " or ")
    expr = expr.replace("-", " not ") # <-- Un reemplazo más robusto

    # 2. Reemplazamos las variables por sus valores
    for var, val in valores.items():
        # Usamos regex para asegurar que solo reemplazamos la variable (p.ej. 'p' y no 'print')
        expr = re.sub(rf'\b{var}\b', str(val), expr)

    # 3. Evaluamos la expresión final de Python
    try:
        # bool() asegura que el resultado de eval() sea True/False
        return bool(eval(expr))
    except Exception as e:
        print(f"Error al evaluar: {expr} | Error: {e}") # Añadido para depurar
        return "Error"

def generar_tabla_html(expresion, variables):
    if not parentesis_balanceados(expresion):
        return "<p style='color:red;'>Error: Paréntesis desbalanceados.</p>"

    filas = list(itertools.product([False, True], repeat=len(variables)))
    html = "<table class='table table-bordered text-center'>"
    html += "<thead class='table-dark'><tr>"

    for v in variables:
        html += f"<th>{v}</th>"
    html += "<th>Resultado</th></tr></thead><tbody>"

    for fila in filas:
        valores = dict(zip(variables, fila))
        resultado = evaluar(expresion, valores)
        html += "<tr>"
        for val in fila:
            html += f"<td>{1 if val else 0}</td>"
        html += f"<td>{'Error' if resultado == 'Error' else int(bool(resultado))}</td>"
        html += "</tr>"

    html += "</tbody></table>"
    return html
