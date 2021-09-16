# type: ignore[name-defined]
"""jack lexer for jack language"""
from sly import Lexer

from .jackerrors import TokenError


class JackLexer(Lexer):
    """Jack Lexer class"""

    tokens = {
        NUMBER, STRING, ID, ASSIGN,
        PLUS, MINUS, MULTIPLY, DIVIDE, SEMI
    }

    ignore = ' \t'
    ignore_comment = r'//.*'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\b[\+-]?[0-9]*[\.]?[0-9]+([eE][\+-]?[0-9]+)?\b'
    ASSIGN = r'='
    # STRING = r'\".*?\"'

    STRING = r'((?<!\\)"[^"\\]*(?: \\.[ ^ "\\]*)*")'

    PLUS = r'\+'
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    MINUS = r'-'

    SEMI = r'\;'

    def error(self, t):
        raise TokenError(f"Illegal character {t.value}")

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
