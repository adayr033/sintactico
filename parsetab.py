
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA DELIMITADOR FINAL IDENTIFICADOR NUMERO_DECIMAL NUMERO_ENTERO OPERADOR PUNTO RESERVADA\n    program : while_loop\n    \n    while_loop : RESERVADA DELIMITADOR condition DELIMITADOR statement_or_block DELIMITADOR\n               | RESERVADA DELIMITADOR condition DELIMITADOR DELIMITADOR statement_or_block DELIMITADOR\n    \n    statement_or_block : statement\n                       | block_statement\n    \n    block_statement : DELIMITADOR statement_list DELIMITADOR\n    \n    statement_list : statement\n                   | statement_list statement\n    \n    statement : println_statement FINAL\n              | condition FINAL\n    \n    println_statement : IDENTIFICADOR DELIMITADOR CADENA DELIMITADOR\n    \n    condition : IDENTIFICADOR OPERADOR NUMERO_ENTERO\n             | IDENTIFICADOR OPERADOR CADENA\n    '
    
_lr_action_items = {'RESERVADA':([0,],[3,]),'$end':([1,2,23,27,],[0,-1,-2,-3,]),'DELIMITADOR':([3,5,7,9,11,12,13,15,16,17,19,20,21,22,24,26,28,29,30,],[4,7,9,18,23,-4,-5,25,-12,-13,27,28,-4,-10,-9,-7,-6,-8,31,]),'IDENTIFICADOR':([4,7,9,18,20,21,22,24,26,29,],[6,15,15,15,15,-7,-10,-9,-7,-8,]),'OPERADOR':([6,15,],[8,8,]),'NUMERO_ENTERO':([8,],[16,]),'CADENA':([8,25,],[17,30,]),'FINAL':([10,14,16,17,31,],[22,24,-12,-13,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'while_loop':([0,],[2,]),'condition':([4,7,9,18,20,],[5,10,10,10,10,]),'statement_or_block':([7,9,],[11,19,]),'statement':([7,9,18,20,],[12,21,26,29,]),'block_statement':([7,9,],[13,13,]),'println_statement':([7,9,18,20,],[14,14,14,14,]),'statement_list':([9,18,],[20,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> while_loop','program',1,'p_program','analizador_sintactico.py',6),
  ('while_loop -> RESERVADA DELIMITADOR condition DELIMITADOR statement_or_block DELIMITADOR','while_loop',6,'p_while_loop','analizador_sintactico.py',12),
  ('while_loop -> RESERVADA DELIMITADOR condition DELIMITADOR DELIMITADOR statement_or_block DELIMITADOR','while_loop',7,'p_while_loop','analizador_sintactico.py',13),
  ('statement_or_block -> statement','statement_or_block',1,'p_statement_or_block','analizador_sintactico.py',35),
  ('statement_or_block -> block_statement','statement_or_block',1,'p_statement_or_block','analizador_sintactico.py',36),
  ('block_statement -> DELIMITADOR statement_list DELIMITADOR','block_statement',3,'p_block_statement','analizador_sintactico.py',42),
  ('statement_list -> statement','statement_list',1,'p_statement_list','analizador_sintactico.py',48),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','analizador_sintactico.py',49),
  ('statement -> println_statement FINAL','statement',2,'p_statement','analizador_sintactico.py',58),
  ('statement -> condition FINAL','statement',2,'p_statement','analizador_sintactico.py',59),
  ('println_statement -> IDENTIFICADOR DELIMITADOR CADENA DELIMITADOR','println_statement',4,'p_println_statement','analizador_sintactico.py',65),
  ('condition -> IDENTIFICADOR OPERADOR NUMERO_ENTERO','condition',3,'p_condition','analizador_sintactico.py',71),
  ('condition -> IDENTIFICADOR OPERADOR CADENA','condition',3,'p_condition','analizador_sintactico.py',72),
]
