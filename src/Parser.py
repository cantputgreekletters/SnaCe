from LexerTokens import *

class Parser:
    def __init__(self, input : list[Token]) -> None:
        self._tk_list : list[Token] = input
        self._current_idx : int = -1
        self._current_token : Token | None = None
        self._forbidden_idx : int = len(self._tk_list)

    def _Advance(self):
        self._current_idx += 1
        self._current_token = self._tk_list[self._current_idx] if self._current_idx < self._forbidden_idx else None

    def __call__(self) -> None: #change type

        self._Advance()
