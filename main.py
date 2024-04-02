from flask import Flask, request, jsonify, render_template
from analizador_lexico import lexer
from analizador_sintactico import analizar_sintaxis

app = Flask('app')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/v1/parser', methods=['POST'])
def parser():
    data = request.get_json()
    code = data.get('code')
    resultado_sintactico = analizar_sintaxis(code)
    return jsonify({'resultado': resultado_sintactico})

@app.route('/api/v1/lexer', methods=['POST'])
def lexer_endpoint():
    data = request.get_json()
    code = data.get('code')
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append({
            'type': tok.type,
            'value': tok.value,
            'line': tok.lineno,
            'lexpos': tok.lexpos
        })

    print("Code:", code)
    print("Tokens:", tokens)

    # Analizar sintaxis
    resultado_sintactico = analizar_sintaxis(code)

    return render_template('result.html', code=code, tokens=tokens, resultado_sintactico=resultado_sintactico)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
