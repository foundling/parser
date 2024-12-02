from ..parser import Parser

def test_parser():
    parser = Parser()
    program = '42'
    ast = parser.parse(program)
    assert ast["body"]["value"] == 42

