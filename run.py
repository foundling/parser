from parser import Parser

parser = Parser()
program = '"hello"' 

ast = parser.parse(program)
print(ast)
