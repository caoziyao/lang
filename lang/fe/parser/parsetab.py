
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftPLUSMINUSleftTIMESDIVIDErightUMINUSCALL COMMENT DEF DIVIDE DOUBLE_EQUAL ELSE EQUAL FALSE ID IF IS_LESS_THEN IS_MORE_THEN LPAREN L_BRACE MINUS NUMBER PLUS PRINT RPAREN R_BRACE STRING THEN TIMES TRUE VAR WHILE l_square_bracket r_square_bracketexpression : IF LPAREN expression RPAREN L_BRACE expression R_BRACE ELSE L_BRACE expression R_BRACEexpression : l_square_bracket  r_square_bracketexpression : ID l_square_bracket NUMBER r_square_bracketexpression : IF LPAREN expression RPAREN L_BRACE expression R_BRACEexpression : DEF func_name LPAREN  RPAREN L_BRACE expression R_BRACEexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EQUAL expression\n    func_name : IDexpression : DEF func_name LPAREN ID RPAREN L_BRACE expression R_BRACEexpression : '-' expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : ID"
    
_lr_action_items = {'IF':([0,3,8,9,10,11,12,13,14,34,35,39,45,],[2,2,2,2,2,2,2,2,2,2,2,2,2,]),'l_square_bracket':([0,3,5,8,9,10,11,12,13,14,34,35,39,45,],[4,4,17,4,4,4,4,4,4,4,4,4,4,4,]),'ID':([0,3,7,8,9,10,11,12,13,14,29,34,35,39,45,],[5,5,19,5,5,5,5,5,5,5,33,5,5,5,5,]),'DEF':([0,3,8,9,10,11,12,13,14,34,35,39,45,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'-':([0,3,8,9,10,11,12,13,14,34,35,39,45,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'LPAREN':([0,2,3,8,9,10,11,12,13,14,18,19,34,35,39,45,],[3,14,3,3,3,3,3,3,3,3,29,-11,3,3,3,3,]),'NUMBER':([0,3,8,9,10,11,12,13,14,17,34,35,39,45,],[6,6,6,6,6,6,6,6,6,28,6,6,6,6,]),'$end':([1,5,6,16,20,21,22,23,24,25,27,31,40,41,44,47,],[0,-16,-15,-2,-13,-6,-7,-8,-9,-10,-14,-3,-4,-5,-12,-1,]),'PLUS':([1,5,6,15,16,20,21,22,23,24,25,26,27,31,37,38,40,41,42,44,46,47,],[9,-16,-15,9,-2,-13,-6,-7,-8,-9,9,9,-14,-3,9,9,-4,-5,9,-12,9,-1,]),'MINUS':([1,5,6,15,16,20,21,22,23,24,25,26,27,31,37,38,40,41,42,44,46,47,],[10,-16,-15,10,-2,-13,-6,-7,-8,-9,10,10,-14,-3,10,10,-4,-5,10,-12,10,-1,]),'TIMES':([1,5,6,15,16,20,21,22,23,24,25,26,27,31,37,38,40,41,42,44,46,47,],[11,-16,-15,11,-2,-13,11,11,-8,-9,11,11,-14,-3,11,11,-4,-5,11,-12,11,-1,]),'DIVIDE':([1,5,6,15,16,20,21,22,23,24,25,26,27,31,37,38,40,41,42,44,46,47,],[12,-16,-15,12,-2,-13,12,12,-8,-9,12,12,-14,-3,12,12,-4,-5,12,-12,12,-1,]),'EQUAL':([1,5,6,15,16,20,21,22,23,24,25,26,27,31,37,38,40,41,42,44,46,47,],[13,-16,-15,13,-2,-13,-6,-7,-8,-9,13,13,-14,-3,13,13,-4,-5,13,-12,13,-1,]),'r_square_bracket':([4,28,],[16,31,]),'RPAREN':([5,6,15,16,20,21,22,23,24,25,26,27,29,31,33,40,41,44,47,],[-16,-15,27,-2,-13,-6,-7,-8,-9,-10,30,-14,32,-3,36,-4,-5,-12,-1,]),'R_BRACE':([5,6,16,20,21,22,23,24,25,27,31,37,38,40,41,42,44,46,47,],[-16,-15,-2,-13,-6,-7,-8,-9,-10,-14,-3,40,41,-4,-5,44,-12,47,-1,]),'L_BRACE':([30,32,36,43,],[34,35,39,45,]),'ELSE':([40,],[43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,8,9,10,11,12,13,14,34,35,39,45,],[1,15,20,21,22,23,24,25,26,37,38,42,46,]),'func_name':([7,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> IF LPAREN expression RPAREN L_BRACE expression R_BRACE ELSE L_BRACE expression R_BRACE','expression',11,'p_condition_if','parse_if.py',7),
  ('expression -> l_square_bracket r_square_bracket','expression',2,'p_array_declar','parse_array.py',9),
  ('expression -> ID l_square_bracket NUMBER r_square_bracket','expression',4,'p_array_access','parse_array.py',15),
  ('expression -> IF LPAREN expression RPAREN L_BRACE expression R_BRACE','expression',7,'p_condition_if_else','parse_if.py',16),
  ('expression -> DEF func_name LPAREN RPAREN L_BRACE expression R_BRACE','expression',7,'p_def','parse_func.py',18),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parse_calc.py',21),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parse_calc.py',22),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parse_calc.py',23),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parse_calc.py',24),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','parse_calc.py',25),
  ('func_name -> ID','func_name',1,'p_def_funcname','parse_func.py',27),
  ('expression -> DEF func_name LPAREN ID RPAREN L_BRACE expression R_BRACE','expression',8,'p_def_arg','parse_func.py',32),
  ('expression -> - expression','expression',2,'p_expression_uminus','parse_calc.py',40),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parse_calc.py',45),
  ('expression -> NUMBER','expression',1,'p_expression_number','parse_calc.py',50),
  ('expression -> ID','expression',1,'p_expression_name','parse_calc.py',55),
]
