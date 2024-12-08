from tokenizer import Tokenizer

class Parser():

    def __init__(self):
        self._tokenizer = Tokenizer()
        self._string = ''

    def parse(self, string):
        self._string = string
        self._tokenizer.init(string)

        self._lookahead = self._tokenizer.getNextToken()

        return self.Program();

    def _eat(self, tokenType):

        token = self._lookahead

        if (token is None):
            raise SyntaxError('unexpected end of input')

        if (token['type'] != tokenType):
            raise SyntaxError(f"unexpected token {token['value']}: expected {tokenType}")
         
        self._lookahead = self._tokenizer.getNextToken()

        return token

    def Program(self):
        '''
        main entry point
        Program
            : StatementList
            | StatementList Statement -> Statement Statement Statement Statement
            ;
        '''
        return {
            'type': 'Program',
            'body': self.StatementList()
        }

    def StatementList(self, stopLookahead=None):

        statementList = [self.Statement()]

        while (self._lookahead is not None and self._lookahead["type"] != stopLookahead):
            statementList.append(self.Statement())

        return statementList

    def Statement(self):
        '''
        Statement
            : ExpressionStatement
            | BlockStatement
            ;

        '''

        if self._lookahead['type'] == '{':
            return self.BlockStatement()
        elif self._lookahead['type'] == ';':
            return self.EmptyStatement();

        return self.ExpressionStatement()

    def EmptyStatement(self):
        '''
            EmptyStatement
                : ';'
                ;

        '''

        self._eat(';')

        return {
            "type": "EmptyStatement"
        }

    def BlockStatement(self):

        self._eat('{')

        body = None
        if self._lookahead["value"] == '}':
            body = []
        else:
            body = self.StatementList('}')

        self._eat('}')

        return {
                "type": "BlockStatement",
                "body": body
        }

    def ExpressionStatement(self):
        '''
        ExpressionStatement
            : Expression ';'
            ;
        '''
        expression = self.Expression()
        self._eat(';')
        return {
            "type": 'ExpressionStatement', 
            "expression": expression,
        }

    def Expression(self):
        '''
            Expression
                : Literal
                ;
        '''
        return self.Literal()

    def Literal(self):

        if self._lookahead["type"] == "STRING":
            return self.StringLiteral()
        elif self._lookahead["type"] == "NUMBER":
            return self.NumericLiteral()
        else:
            raise SyntaxError("Literal: unexpected literal production")

    def StringLiteral(self):

        token = self._eat('STRING')
        return {
            "type": "StringLiteral",
            "value": token["value"][1:-1]
        }

    def NumericLiteral(self):
        '''
        NumericLiteral
            : Number
            ;
        '''
        token = self._eat('NUMBER')

        return {
            "type": "NumericLiteral",
            "value": int(token['value'])
        }
