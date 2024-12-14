from parser.src.parser import Parser
import pytest


@pytest.fixture
def parser():
    return Parser()

def test_binary_expression(parser):

    program = '2 + 2;'
    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [
            {
                "type": "ExpressionStatement",
                "expression": {
                    "type": "BinaryExpression",
                    "operator": '+',
                    "left": {
                        "type": "NumericLiteral",
                        "value": 2
                    },
                    "right": {
                        "type": "NumericLiteral",
                        "value": 2
                    }
                }
            }
        ]
    }


def test_nested_binary_expression(parser):

    program = '3 + 2 - 2;'
    ast = parser.parse(program)

    assert ast == {
        "type": "Program",
        "body": [
            {
                "type": "ExpressionStatement",
                "expression": {
                    "type": "BinaryExpression",
                    "operator": '-',
                    "left": {
                        "type": "BinaryExpression",
                        "operator": "+",
                        "left": {
                            "type":"NumericLiteral",
                            "value": 3
                        },
                        "right": {
                            "type":"NumericLiteral",
                            "value": 2
                        }
                    },
                    "right": {
                        "type": "NumericLiteral",
                        "value": 2
                    }
                }
            }
        ]
    }

def test_multiplicative_expression(parser):

    program = '2 + 2 * 2;'
    ast = parser.parse(program)

    assert ast == {

        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "BinaryExpression",
                "operator": "+",
                "left": {
                    "type": "NumericLiteral",
                    "value": 2
                },
                "right": {
                    "type": "BinaryExpression",
                    "operator": "*",
                    "left": {
                        "type": "NumericLiteral",
                        "value": 2,
                    },
                    "right": {
                        "type": "NumericLiteral",
                        "value": 2
                    }
                }
            }
        }]

    }


def test_multiplicative_expression2(parser):

    program = '2 * 2 * 2;'
    ast = parser.parse(program)

    assert ast == {

        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "BinaryExpression",
                "operator": "*",
                "left": {
                    "type": "BinaryExpression",
                    "operator": "*",
                    "left": {
                        "type": "NumericLiteral",
                        "value": 2,
                    },
                    "right": {
                        "type": "NumericLiteral",
                        "value": 2
                    }
                },
                "right": {
                    "type": "NumericLiteral",
                    "value": 2
                }
            }
        }]

    }


def test_multiplicative_expression3(parser):

    program = '2 * 2 + 2;'
    ast = parser.parse(program)

    assert ast == {

        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "BinaryExpression",
                "operator": "+",
                "left": {
                    "type": "BinaryExpression",
                    "operator": "*",
                    "left": {
                        "type": "NumericLiteral",
                        "value": 2,
                    },
                    "right": {
                        "type": "NumericLiteral",
                        "value": 2
                    }
                },
                "right": {
                    "type": "NumericLiteral",
                    "value": 2
                }
            }
        }]

    }



def test_parenthesized_expression(parser):

    program = '(2 + 2) * 2'
    ast = parser.parse(program)

    assert ast == {

        "type": "Program",
        "body": [{
            "type": "ExpressionStatement",
            "expression": {
                "type": "BinaryExpression",
                "operator": "*",
                "left": {
                    "type": "BinaryExpression",
                    "operator": "+",
                    "left": {
                        "type": "NumericLiteral",
                        "value": 2,
                    },
                    "right": {
                        "type": "NumericLiteral",
                        "value": 2
                    }
                },
                "right": {
                    "type": "NumericLiteral",
                    "value": 2
                }
            }
        }]


    }
