from parser import Parser

parser = Parser()
program = '''
    42
    "hello"
/*
* a multi-line comment
*/

// hi
'''
ast = parser.parse(program)
print(ast)
