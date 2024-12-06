from parser import Parser
import pprint
import json

parser = Parser()
program = '42; "hello"; /* asdf */'
ast = parser.parse(program)
json = json.dumps(ast)
print(json)
