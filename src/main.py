from ast import BinOp, Del
from Lexer import Lexer
from Parser import Parser,BinOp
from Interpreter import Interpreter

DEBUG = True

if __name__ == "__main__": #its likes this for now just for testing
    text = "3 * 2 + 1 * 8"
    lexer = Lexer(text)
    re, error = lexer()
    if DEBUG:
        print(f"Lexer results:\n{re}")
    if (error):
        print(error)
        quit(-1)
    parser = Parser(re)
    re = parser()
    if DEBUG:
        print(f"Parser results:\n{re}")
    if DEBUG:
        print("Interpreter results:")
    if isinstance(re, BinOp):
        intr = Interpreter(re)
        print(intr())
