
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE DOUBLE_EQUAL ELSE EQUAL FALSE ID IF LPAREN MINUS NUMBER PLUS PRINT RPAREN STRING THEN TIMES TRUE VAR WHILEexpression : expression PLUS termexpression : id EQUAL expressionexpression : print valueexpression : expression MINUS termid : IDprint : PRINTexpression : termvalue : STRINGterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBER\n    factor : LPAREN expression RPAREN'
    
_lr_action_items = {'ID':([0,9,14,],[5,5,5,]),'PRINT':([0,9,14,],[6,6,6,]),'NUMBER':([0,9,10,11,12,13,14,],[8,8,8,8,8,8,8,]),'LPAREN':([0,9,10,11,12,13,14,],[9,9,9,9,9,9,9,]),'$end':([1,2,7,8,15,16,18,19,20,21,22,23,],[0,-7,-11,-12,-3,-8,-1,-4,-9,-10,-2,-13,]),'PLUS':([1,2,7,8,15,16,17,18,19,20,21,22,23,],[10,-7,-11,-12,-3,-8,10,-1,-4,-9,-10,10,-13,]),'MINUS':([1,2,7,8,15,16,17,18,19,20,21,22,23,],[11,-7,-11,-12,-3,-8,11,-1,-4,-9,-10,11,-13,]),'RPAREN':([2,7,8,15,16,17,18,19,20,21,22,23,],[-7,-11,-12,-3,-8,23,-1,-4,-9,-10,-2,-13,]),'TIMES':([2,7,8,18,19,20,21,23,],[12,-11,-12,12,12,-9,-10,-13,]),'DIVIDE':([2,7,8,18,19,20,21,23,],[13,-11,-12,13,13,-9,-10,-13,]),'EQUAL':([3,5,],[14,-5,]),'STRING':([4,6,],[16,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,9,14,],[1,17,22,]),'term':([0,9,10,11,14,],[2,2,18,19,2,]),'id':([0,9,14,],[3,3,3,]),'print':([0,9,14,],[4,4,4,]),'factor':([0,9,10,11,12,13,14,],[7,7,7,7,20,21,7,]),'value':([4,],[15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parse_calculation.py',15),
  ('expression -> id EQUAL expression','expression',3,'p_assignment','parse_assignment.py',16),
  ('expression -> print value','expression',2,'p_print','parse_print.py',17),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parse_calculation.py',20),
  ('id -> ID','id',1,'p_assignment_id','parse_assignment.py',21),
  ('print -> PRINT','print',1,'p_print_print','parse_print.py',22),
  ('expression -> term','expression',1,'p_expression_term','parse_calculation.py',25),
  ('value -> STRING','value',1,'p_print_value','parse_print.py',27),
  ('term -> term TIMES factor','term',3,'p_term_times','parse_calculation.py',30),
  ('term -> term DIVIDE factor','term',3,'p_term_div','parse_calculation.py',36),
  ('term -> factor','term',1,'p_term_factor','parse_calculation.py',41),
  ('factor -> NUMBER','factor',1,'p_factor_num','parse_calculation.py',46),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parse_calculation.py',53),
]