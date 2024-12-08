from src import parser
import json

parser = parser.Parser()
program = '''
{
    42;
}
'''
ast = parser.parse(program)
json = json.dumps(ast)
print(json)
