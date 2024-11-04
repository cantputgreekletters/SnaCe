from LexerTokens import *
from ParserNodes import *
from typing import Self

EXPRESSION_OP = ['+', '-']
TERM_OP = ['*','/']
FACTOR_TK = [TOKEN_INT, TOKEN_FLOAT, TOKEN_WORD]
class BinOp:
    def __init__(self, left_node : Token | Self | None, op : Token | None, right_node : Token | Self | None) -> None:
        self._left_node : Token | Self | None = left_node
        self._op : Token | None = op
        self._right_node : Token | Self | None = right_node

    @property
    def op(self): return self._op

    @op.getter
    def op(self) -> Token | None : return self._op

    def __repr__(self) -> str:
        return f"[L : {self._left_node}, OP: {self._op}, R : {self._right_node}]"

class Parser:
    def __init__(self, input : list[Token]) -> None:
        self._tk_list : list[Token] = input
        self._current_idx : int = -1
        self._current_token : Token | None = None
        self._forbidden_idx : int = len(self._tk_list)
        self._error : str | None = None

    def _GetNextToken(self) -> Token | None:
        tk = None
        if self._current_idx + 1 < self._forbidden_idx:
            tk =  self._tk_list[self._current_idx + 1]
        return tk

    def _GetPreviousToken(self) -> Token | None:
        tk = None
        if 0 <= self._current_idx - 1:
            tk =  self._tk_list[self._current_idx - 1]
        return tk
    def _Advance(self):
        self._current_idx += 1
        self._current_token = self._tk_list[self._current_idx] if self._current_idx < self._forbidden_idx else None

    def _factor(self) -> BinOp | Token | None:
        tk : Token | None = self._current_token

        if not tk:
            self._error = "Invalid token"
            return

        self._Advance()
        return tk

    def _term(self) -> BinOp | Token | None:
        left = self._factor()
        while self._current_token != None and self._current_token.value in TERM_OP:
            op : Token = self._current_token
            self._Advance()
            right = self._factor()
            if not right:
                self._error = "Empty right operrand"
                return
            return BinOp(left, op, right)
        return left

    def _expression(self) -> BinOp | Token | None:
        left = self._term()
        while self._current_token != None and self._current_token.value in EXPRESSION_OP:
            op : Token = self._current_token
            self._Advance()
            right = self._term()
            if not right:
                self._error = "Operator with no right operrand"
                return
            return BinOp(left, op, right)

        return left

    def __call__(self) -> BinOp | Token | None: #change type
        self._Advance()
        re : BinOp | Token | None = self._expression()
        return re

#Parser output is wrong
