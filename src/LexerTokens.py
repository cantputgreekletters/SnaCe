#Token types
TOKEN_INT = "TOKEN_INT"
TOKEN_FLOAT = "TOKEN_FLOAT"
TOKEN_WORD = "TOKEN_WORD"
TOKEN_LPAREN = "TOKEN_LPAREN"
TOKEN_RPAREN = "TOKEN_RPAREN"
TOKEN_QUOTE = "TOKEN_QUOTE"
TOKEN_COMMA = "TOKEN_COMMA"
TOKEN_OPERATOR = "TOKEN_OPERATOR"
TOKEN_ERROR = "TOKEN_ERROR"
TOKEN_EOL = "TOKEN_EOL"
TOKEN_LBRACKET = "TOKEN_LBRACKET"
TOKEN_RBRACKET = "TOKEN_RBRACKET"
#=====================================
class Token:
    def __init__(self, type : str, value : str | None = None) -> None:
        self._type = type
        self._value = value

    def __repr__(self) -> str:
        return f"({self._type} : '{self._value}')" if self._value else f"({self._type})"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def value(self) -> str | None:
        return self._value

    @value.getter
    def value(self) -> str | None:
        return self._value

    @property
    def type(self) -> str | None:
        return self._type

    @type.getter
    def type(self) -> str | None:
        return self._type
