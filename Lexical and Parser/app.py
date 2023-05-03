from lex import *
from parse import *
import sys


def main():
    print("Hello To Python Compiler!")
    with open("comparison.txt", 'r') as inputFile:
        source = inputFile.read()

    # The lexer
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(f"{token.text}  ===> {token.kind}")
        token = lexer.getToken()

    # Initialize the lexer and parser.
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program() # Start the parser.
    print("Parsing completed.")

main()