from LexerTokens import *

IGNORE_CHARACTERS : list[str] = [" ", "\t",]
NUMBERS : set[str] = "1234567890" #type: ignore
NUMBERS = {i for i in NUMBERS}
OPERATORS : set[str] = "+-/*=" #type: ignore
OPERATORS = {i for i in OPERATORS}
EOL = ';'
BANNED_INIT_CHARACTER : set[str] = "!@#$%^&*{}[]:?/`~" #type: ignore
BANNED_INIT_CHARACTER = {i for i in BANNED_INIT_CHARACTER}
BANNED_INIT_CHARACTER ^= OPERATORS ^ NUMBERS ^ {EOL}
class Lexer:
    def __init__(self, text : str) -> None:
        self._text : str = text
        self._current_idx : int = -1
        self._forbidden_idx : int = len(text)
        self._current_character : str | None = ""
        self._error : str | None = None

    def _Advance(self):
        self._current_idx += 1
        self._current_character = self._text[self._current_idx] if self._current_idx < self._forbidden_idx else None

    def _HandleNumeric(self) -> Token:
        point_counter : int = 0
        number : str = "" #type: ignore
        while self._current_character and self._current_character in NUMBERS:
            number += self._current_character
            if self._current_character == ".":
                point_counter += 1
            self._Advance()

        self._current_idx -= 1 #after returning it will skip a value if this does not get set back by one
        tk_type : str
        if point_counter > 1:
            self._error = "Point counter > 1"
            tk_type = TOKEN_ERROR
        elif point_counter == 1:
            tk_type = TOKEN_FLOAT
        else:
            tk_type = TOKEN_INT
        return Token(tk_type, number)

    def _HandleWords(self) -> Token:
        if self._current_character in BANNED_INIT_CHARACTER:
            self._error = f"First character is not allowed: '{self._current_character}'"
            return Token(TOKEN_ERROR, self._current_character)

        word : str = ""
        while self._current_character and self._current_character not in IGNORE_CHARACTERS:
            word += self._current_character
            self._Advance()
        self._current_idx -= 1 #after returning it will skip a value if this does not get set back by one
        return Token(TOKEN_WORD, word)
    def __call__(self) -> tuple[list[Token],str | None]:
        token_list : list[Token] = []
        self._Advance()
        while self._current_character != None and self._error == None:
            if self._current_character in IGNORE_CHARACTERS:
                pass
            elif self._current_character in NUMBERS:
                token_list.append(self._HandleNumeric())
            elif self._current_character == "(":
                token_list.append(Token(TOKEN_LPAREN, '('))
            elif self._current_character == ")":
                token_list.append(Token(TOKEN_RPAREN, ')'))
            elif self._current_character == '{':
                token_list.append(Token(TOKEN_LBRACKET, '{'))
            elif self._current_character == '}':
                token_list.append(Token(TOKEN_RBRACKET, '}'))
            elif self._current_character in OPERATORS:
                token_list.append(Token(TOKEN_OPERATOR, self._current_character))
            elif self._current_character == EOL:
                token_list.append(Token(TOKEN_EOL, EOL))
            elif self._current_character == ',':
                token_list.append(Token(TOKEN_COMMA, ','))
            elif self._current_character == '"':
                token_list.append(Token(TOKEN_QUOTE, '"'))
            elif self._current_character.isascii(): #is a word
                token_list.append(self._HandleWords())
            else:
                self._error = "Invalid Character"
                token_list.append(Token(TOKEN_ERROR, self._current_character))
            self._Advance()

        return token_list, self._error


if __name__ == "__main__":
    lexer = Lexer("hello + 3")
    re,error = lexer()
    print(f"re = {re}, error = {error}")
