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

    def Statement(self):
        '''
        Statement
            : ExpressionStatement
            ;

        '''
        return self.ExpressionStatement()

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

    def StatementList(self):

        statementList = [self.Statement()]

        while (self._lookahead is not None):
            statementList.append(self.Statement())

        return statementList

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
