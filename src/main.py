from ast import BinOp, Del
from Lexer import Lexer
from Parser import Parser,BinOp
from Interpreter import Interpreter

DEBUG = True

def RunOnTerminal():
    print("Running SnaCe")
    print("Enter 'q' to exit")
    text = "1 + 1"
    while text != "q":
        text = str(input())
        lexer = Lexer(text)
        re, error = lexer()
        if DEBUG:
            print(f"Lexer results:\n{re}")
        if (error):
            print(error)
            quit(-1)
        parser = Parser(re)
        re,error = parser()
        if error:
            print(error)
            quit(-1)
        if DEBUG:
            print(f"Parser results:\n{re}")
        if DEBUG:
            print("Interpreter results:")
        if isinstance(re, BinOp):
            intr = Interpreter(re)
            re, error = intr()
            if error:
                print(error)
                quit(-1)
            print(re)

if __name__ == "__main__": #its likes this for now just for testing
    RunOnTerminal()
