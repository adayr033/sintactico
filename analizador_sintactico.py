import ply.yacc as yacc
from analizador_lexico import tokens

def p_program(p):
    '''
    program : while_loop
    '''
    p[0] = p[1]

def p_while_loop(p):
    '''
    while_loop : RESERVADA DELIMITADOR condition DELIMITADOR statement_or_block DELIMITADOR
               | RESERVADA DELIMITADOR condition DELIMITADOR DELIMITADOR statement_or_block DELIMITADOR
    '''
    if len(p) == 6:
        p[0] = [
            "Bucle While válido:",
            str(p[3]),        # Condición
            "{",
            str(p[5]),        # Declaración de impresión
            "}"
        ]
    else:
        p[0] = [
            "Bucle While válido:",
            str(p[3]),        # Condición
            "{",
            "}",
            str(p[5]),        # Declaración de impresión
            "}"
        ]

def p_statement_or_block(p):
    '''
    statement_or_block : statement
                       | block_statement
    '''
    p[0] = p[1]

def p_block_statement(p):
    '''
    block_statement : DELIMITADOR statement_list DELIMITADOR
    '''
    p[0] = p[2]

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''
    statement : println_statement FINAL
              | condition FINAL
    '''
    p[0] = p[1]

def p_println_statement(p):
    '''
    println_statement : IDENTIFICADOR DELIMITADOR CADENA DELIMITADOR
    '''
    p[0] = f"Declaración de impresión válida: {p[1]}({p[3]})"

def p_condition(p):
    '''
    condition : IDENTIFICADOR OPERADOR NUMERO_ENTERO
             | IDENTIFICADOR OPERADOR CADENA
    '''
    p[0] = f"Condición válida: {p[1]} {p[2]} {p[3]}"

def p_error(p):
    if p:
        print(f"Error de sintaxis en la línea {p.lineno}: Valor inesperado '{p.value}'")
    else:
        print("Error de sintaxis: entrada incompleta o incorrecta")

parser = yacc.yacc()

def analizar_sintaxis(codigo):
    try:
        resultado = parser.parse(codigo)
        if resultado is not None:  # Comprobar si el resultado no es None
            return resultado
        else:
            return "Error de sintaxis: entrada vacía"
    except Exception as e:
        return f"Error de sintaxis: {str(e)}"
