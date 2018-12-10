# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/12/6 
@desc:
descent_parsing 递归下降
算法基本思想
每个非终结符构造一个分析函数
用前看符号指导产生式规则的规则
"""
from parser_descent.src.token import Type
from parser_descent.src.expression import ExpInt, ExpAdd, ExpTimes, Kind, ExpDiv


# current_index = 0

class TokenList(object):

    def __init__(self, tokens=None):
        self.index = 0
        self.tokens = tokens

    def current(self):

        if self.isend():
            t = None
        else:
            t = self.tokens[self.index]

        return t

    def size(self):
        """
        :return:
        """
        return len(self.tokens)

    def isend(self):
        """
        :return:
        """
        return self.index == self.size()

    def get_token(self):
        """
        :return:
        """
        t = self.tokens[self.index]
        self.index += 1
        return t

    def lookahead(self):
        """
        :return:
        """
        if self.isend():
            t = None
        else:
            t = self.tokens[self.index + 1]

        return t


tokens = TokenList()


def valid_keyword(token, name):
    """

    :param name:
    :return:
    """
    kind = token.type
    value = token.value

    if kind == Type.keyword and value == name:
        return True
    else:
        return False


def match(token, name=''):
    pass


def optexpr():
    """
    :return:
    """
    t = tokens.current()

    kind = t.type
    value = t.value

    if kind == Type.id:
        pass


def parse_factor():
    """
    factor -> digit | ( expr )
    :return:
    """
    t = tokens.get_token()
    kind = t.type
    value = t.value

    if kind == Type.number:
        return value
    elif kind == Type.parenthesesLeft:
        value = parse_expr()
        tokens.get_token()
        return value
    else:
        raise Exception('expect number but {}'.format(value))


def parse_term():
    """
    term -> term * factor | term / factor | factor
    :return:
    """

    res = parse_factor()

    t = tokens.current()
    if t is None:
        return res

    kind = t.type
    value = t.value

    while kind in [Type.times, Type.div]:
        tokens.get_token()

        if kind == Type.times:
            right = parse_factor()
            res *= right
        elif kind == Type.div:
            right = parse_factor()
            res /= right

        t = tokens.current()
        if t is None:
            break

        kind = t.type
        value = t.value

    # if t is not None:
    #     raise Exception('expect */ but {} {}'.format(kind, value))

    return res


def parse_expr():
    """
    1 + 2 * 3
    表达式 expr ::= term { (+|-) term }*
    :return:
    """
    res = parse_term()

    t = tokens.current()
    if t is None:
        return res

    kind = t.type
    value = t.value
    while kind in [Type.add, Type.sub]:
        tokens.get_token()

        if kind == Type.add:
            right = parse_term()
            res += right
        elif kind == Type.sub:
            right = parse_term()
            res -= right

        t = tokens.current()
        if t is None:
            break

        kind = t.type
        value = t.value

    # if t is not None:
    #     raise Exception('expect +- but {} {}'.format(kind, value))

    return res


def parse_stmt():
    """
    a = 1 + 2 * 3
    :param token_list:
    :return:
    """
    tokens.get_token()  # id
    assign = tokens.get_token()  # =
    kind = assign.type
    value = assign.value

    if kind == Type.assign:
        expr = parse_expr()
    else:
        raise Exception('expect = but {}'.format(value))

    print('expr', expr)


def parse_for():
    """

    :return:
    """
    t = tokens.current()
    kind = t.type
    value = t.value

    if valid_keyword(t, 'for'):
        # for ( ; ; ;) {}
        match(t, 'for')  # for
        match(t, '(')  # (
        optexpr()  #
        match(t, ';')  # ;
        optexpr()  #
        match(t, ';')  # ;
        optexpr()  #
        match(t, ';')  # ;
        match(t, ')')  # )
        match(t, '{')  # {
        optexpr()  #
        match(t, '}')  # }

    elif kind == Type.id:
        optexpr()


def syntax_analysis(token_list):
    """
    :param token_list:
    :return:
    """
    tokens.tokens = token_list

    t = tokens.current()
    kind = t.type
    value = t.value

    if kind == Type.id:
        parse_stmt()
    elif kind == Type.keyword and value == 'for':
        parse_for()
