from ..parser import Parser
import pytest


@pytest.fixture
def parser():
    return Parser()

def test_block(parser):

    program = '''
    {
        42;
    }
    '''

    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "BlockStatement",
            "body": [{
                "type": "ExpressionStatement", 
                "expression": {
                    "type": "NumericLiteral",
                    "value": 42
                }
            }]
        }]
    }

def test_empty_block(parser):

    program = '''
    {
    }
    '''

    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "BlockStatement",
            "body": []
        }]
    }

def test_nested_blocks(parser):

    program = '''
    {
        {
            42;"hello";
        }
    }
    '''

    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [{
            "type": "BlockStatement",
            "body": [{
                "type": "BlockStatement",
                "body": [
                    {
                        "type": "ExpressionStatement",
                        "expression": {
                            "type": "NumericLiteral",
                            "value": 42
                        }
                    },
                    {
                        "type": "ExpressionStatement",
                        "expression": {
                            "type": "StringLiteral",
                            "value": 'hello'
                        }
                    }
                ]

            }]
        }]
    }
