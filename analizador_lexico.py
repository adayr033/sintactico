import ply.lex as lex

tokens = (
    'RESERVADA',
    'IDENTIFICADOR',
    'DELIMITADOR',
    'OPERADOR',
    'NUMERO_ENTERO',
    'PUNTO',
    'NUMERO_DECIMAL',
    'FINAL',
    'CADENA'
)

palabras_reservadas = ['while', 'static', 'void', 'int', 'public', 'main', 'for', 'do', 'if', 'else']

# Expresiones regulares para tokens
t_OPERADOR = r'>='
t_PUNTO = r'\.'
t_FINAL = r';'
t_DELIMITADOR = r'[(){}\[\]]'

# Función para identificar identificadores y palabras reservadas
def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = 'RESERVADA' if t.value.lower() in [reservada.lower() for reservada in palabras_reservadas] else 'IDENTIFICADOR'
    return t

# Función para identificar números enteros
def t_NUMERO_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Función para identificar números decimales
def t_NUMERO_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Función para identificar cadenas
def t_CADENA(t):
    r'"([^"]*)"'
    return t

# Ignorar espacios en blanco
t_ignore = ' \t'

# Función para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Función para manejar errores léxicos
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
