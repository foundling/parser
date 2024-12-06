from ..parser import Parser




def test_string_literal_single_quote():

    program = '"hello, world!";'
    p = Parser()
    ast = p.parse(program)

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

def test_numeric_literal():

    program = '''42;'''
    p = Parser()
    ast = p.parse(program)

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

def test_string_literal_double_quote():
    program = "'hello, world!';"
    p = Parser()
    ast = p.parse(program)
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

