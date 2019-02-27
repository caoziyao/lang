
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftPLUSMINUSleftTIMESDIVIDErightUMINUSCALL COMMENT DEF DIVIDE DOUBLE_EQUAL ELSE EQUAL FALSE ID IF IS_LESS_THEN IS_MORE_THEN LPAREN L_BRACE MINUS NUMBER PLUS PRINT RPAREN R_BRACE STRING THEN TIMES TRUE VAR WHILEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : '-' expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : ID"
    
_lr_action_items = {'-':([0,2,3,6,7,8,9,],[2,2,2,2,2,2,2,]),'LPAREN':([0,2,3,6,7,8,9,],[3,3,3,3,3,3,3,]),'NUMBER':([0,2,3,6,7,8,9,],[4,4,4,4,4,4,4,]),'ID':([0,2,3,6,7,8,9,],[5,5,5,5,5,5,5,]),'$end':([1,4,5,10,12,13,14,15,16,],[0,-7,-8,-5,-1,-2,-3,-4,-6,]),'PLUS':([1,4,5,10,11,12,13,14,15,16,],[6,-7,-8,-5,6,-1,-2,-3,-4,-6,]),'MINUS':([1,4,5,10,11,12,13,14,15,16,],[7,-7,-8,-5,7,-1,-2,-3,-4,-6,]),'TIMES':([1,4,5,10,11,12,13,14,15,16,],[8,-7,-8,-5,8,8,8,-3,-4,-6,]),'DIVIDE':([1,4,5,10,11,12,13,14,15,16,],[9,-7,-8,-5,9,9,9,-3,-4,-6,]),'RPAREN':([4,5,10,11,12,13,14,15,16,],[-7,-8,-5,16,-1,-2,-3,-4,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,6,7,8,9,],[1,10,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parse_calc.py',25),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parse_calc.py',26),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parse_calc.py',27),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parse_calc.py',28),
  ('expression -> - expression','expression',2,'p_expression_uminus','parse_calc.py',40),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parse_calc.py',45),
  ('expression -> NUMBER','expression',1,'p_expression_number','parse_calc.py',50),
  ('expression -> ID','expression',1,'p_expression_name','parse_calc.py',55),
]