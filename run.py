from src import parser
import json

parser = parser.Parser()
program = '''
{
    (2 + 2) * 2;
}
'''
ast = parser.parse(program)
json = json.dumps(ast)
print(json)
