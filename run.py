from src import parser
import json

parser = parser.Parser()
program = '''
{
    3 + 2 - 2;
}
'''
ast = parser.parse(program)
json = json.dumps(ast)
print(json)
