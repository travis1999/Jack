import pytest
from jack import jacklexer
from jack import jackerrors


@pytest.fixture
def lexer():
    return jacklexer.JackLexer()


def get_tokens(lexer, token_string):
    tok_stream = lexer.tokenize(token_string)
    return list(tok_stream)


def get_single_token(lexer, token_string):
    tok_stream = lexer.tokenize(token_string)
    return list(tok_stream)[0]


def test_number(lexer):
    token = get_single_token(lexer, "5")
    assert token.type == "NUMBER"
    assert token.value == "5"

    token = get_single_token(lexer, "1000000.1")
    assert token.type == "NUMBER"
    assert token.value == "1000000.1"

    token = get_single_token(lexer, "1.0e-05")
    assert token.type == "NUMBER"
    assert token.value == "1.0e-05"


def test_string(lexer):
    token = get_single_token(lexer, '"hello"')
    assert token.type == "STRING"
    assert token.value == '"hello"'

    token = get_single_token(lexer, '"\thello, \t \t world\n"')
    assert token.type == "STRING"
    assert token.value == '"\thello, \t \t world\n"'


def test_symbols(lexer):
    tokens = get_tokens(lexer, "+-*/=;")

    token_names = ["PLUS", "MINUS", "MULTIPLY",
                   "DIVIDE", "ASSIGN", "SEMI"]

    token_values = ["+", "-", "*", "/", "=", ";"]

    for tok, tok_name, tok_value in zip(tokens, token_names, token_values):
        assert tok.type == tok_name
        assert tok.value == tok_value


def test_lex_error(lexer):
    with pytest.raises(jackerrors.TokenError):
        get_tokens(lexer, "5&")


def test_ignore_newline(lexer):
    tokens = get_tokens(lexer, "1\n2\n3\n")
    assert tokens[2].lineno == 3
