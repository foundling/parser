from parser import Parser

parser = Parser()
program = '''
    42
// comment
'''
ast = parser.parse(program)
print(ast)
