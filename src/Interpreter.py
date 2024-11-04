from re import NOFLAG
from LexerTokens import Token
from Parser import BinOp

class Interpreter:
    def __init__(self, bin_op : BinOp) -> None:
        self._bin_op : BinOp = bin_op
        self._error : str | None = None

    def _process_nodes(self, a : Token | None | BinOp, b : Token | None | BinOp) -> None | tuple[int | float, int | float]:
        if not (a and b):
            self._error = "Cant operate on None-type"
        A : int | float | None = None
        B : int | float | None = None
        if isinstance(a,BinOp):
            A = self._solve_operator(a)
        elif isinstance(a, Token):
            A = a.TurnToNumber()
        if isinstance(b,BinOp):
            B = self._solve_operator(b)
        elif isinstance(b, Token):
            B = b.TurnToNumber()
        if A == None or B == None:
            self._error = "Cant operate on None-type"
            return
        return A,B
    def _add(self, a : Token | None | BinOp, b : Token | None | BinOp) -> int | float | None:
        re : None | tuple[int | float, int | float] = self._process_nodes(a,b)
        if not re:
            self._error = "Cant add None-type"
            return
        A,B = re
        return A + B

    def _subtract(self, a : Token | None | BinOp, b : Token | None | BinOp):
        re : None | tuple[int | float, int | float] = self._process_nodes(a,b)
        if not re:
            self._error = "Cant subtract None-type"
            return
        A,B = re
        return A - B

    def _multiply(self, a : Token | None | BinOp, b : Token | None | BinOp):
        re : None | tuple[int | float, int | float] = self._process_nodes(a,b)
        if not re:
            self._error = "Cant multiply None-type"
            return
        A,B = re
        return A * B

    def _divide(self, a : Token | None | BinOp, b : Token | None | BinOp):
        re : None | tuple[int | float, int | float] = self._process_nodes(a,b)
        if not re:
            self._error = "Cant divide None-type"
            return
        A,B = re
        if B == 0:
            self._error = "Cant divide with zero"
            return
        return A / B

    def _solve_operator(self, op : BinOp) -> int | float | None:
        if not op:
            return
        operator : str | None = op.op.value #type: ignore
        match operator:
            case '+':
                f = self._add
            case '-':
                f = self._subtract
            case '/':
                f = self._divide
            case '*':
                f = self._multiply
            case _:
                f = None
        if not f:
            self._error = "not valid operator"
            return
        return f(op._left_node, op._right_node)


    def __call__(self) -> int | float | None:
        return self._solve_operator(self._bin_op)
