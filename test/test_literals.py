from ..parser import Parser
import pytest


@pytest.fixture
def parser():
    return Parser()

def test_string_literal_single_quote(parser):

    program = '"hello, world!";'
    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "StringLiteral",
                "value": 'hello, world!'
            }
        }]
    }

def test_numeric_literal(parser):

    program = '''42;'''
    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "NumericLiteral",
                "value": 42
            }
        }]
    }

def test_string_literal_double_quote(parser):

    program = "'hello, world!';"
    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "StringLiteral",
                "value": 'hello, world!'
            }
        }]
    }

