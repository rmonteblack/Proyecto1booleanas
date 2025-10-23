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
    for var, val in valores.items():
        expr = re.sub(rf'\b{var}\b', str(val), expr)

    expr = expr.replace("<->", "==")
    expr = expr.replace("->", " or not ")
    expr = expr.replace("^", " and ")
    expr = expr.replace("||", " or ")
    expr = re.sub(r'-\s*(True|False)', r'not \1', expr)

    try:
        return eval(expr)
    except Exception:
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
