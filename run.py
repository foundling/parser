from parser import Parser

parser = Parser()
program = '" hello, world! "'

ast = parser.parse(program)
print(ast)
