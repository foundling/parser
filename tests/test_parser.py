from ..parser import Parser

def test_parser():
    ast = Parser().parse('25')
    assert ast['value'] == 25
    assert ast['type'] == 'NumericLiteral'
