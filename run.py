from parser import Parser
import pprint
import json

parser = Parser()
program = '''
{
    42;
}
'''
ast = parser.parse(program)
json = json.dumps(ast)
print(json)
