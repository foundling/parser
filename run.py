from parser import Parser

parser = Parser()
ast = parser.parse(" 42 ")
print(ast)
