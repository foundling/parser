from ..parser import Parser
import pytest


@pytest.fixture
def parser():
    return Parser()

def test_string_literal_single_quote(parser):

    program = '''

    "hello, world!";

    42;

    '''
    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [
            {
                "type": "ExpressionStatement",
                "expression": {
                    "type": "StringLiteral",
                    "value": 'hello, world!'
                }
            },
            {
                "type": "ExpressionStatement",
                "expression": {
                    "type": "NumericLiteral",
                    "value": 42
                }
            }
        ]
    }
