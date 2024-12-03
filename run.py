from parser import Parser

parser = Parser()
#program = "'hello'";
program = "'hello'";

ast = parser.parse(program)
print(ast)
