from .tokenizer import Tokenizer

AST_MODE = 'default'


class DefaultFactory():

    def Program(self, body):
        return {
            "type": "Program",
            "body": body
        }

    def EmptyStatement(self):
        return {
            "type": "EmptyStatement"
        }

    def BlockStatement(self, body):
        return {
            "type": "BlockStatement",
            "body": body
        }

    def ExpressionStatement(self, expression):
        return {
            "type": 'ExpressionStatement',
            "expression": expression,
        }

    def StringLiteral(self, value):
        return {
            "type": "StringLiteral",
            "value": value,
        }

    def NumericLiteral(self, value):
        return {
            "type": "NumericLiteral",
            "value": value
        }

    def BinaryExpression(self, left, right):
        return {
            "type": "BinaryExpression",
            "operator": "+",
            "left": self.NumericLiteral(left),
            "right": self.NumericLiteral(right)
        }


factory = None
if AST_MODE == 'default':
    factory = DefaultFactory()


class Parser():

    def __init__(self):
        self._tokenizer = Tokenizer()
        self._string = ''

    def parse(self, string):
        self._string = string
        self._tokenizer.init(string)

        self._lookahead = self._tokenizer.getNextToken()

        return self.Program()

    def _eat(self, tokenType):

        token = self._lookahead

        if (token is None):
            raise SyntaxError('unexpected end of input')

        if (token['type'] != tokenType):
            raise SyntaxError(
                f"unexpected token {token['value']}: expected {tokenType}")

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
        return factory.Program(self.StatementList())

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
            return self.EmptyStatement()

        return self.ExpressionStatement()

    def EmptyStatement(self):
        '''
            EmptyStatement
                : ';'
                ;

        '''

        self._eat(';')

        return factory.EmptyStatement()

    def BlockStatement(self):

        self._eat('{')

        body = None
        if self._lookahead["value"] == '}':
            body = []
        else:
            body = self.StatementList('}')

        self._eat('}')

        return factory.BlockStatement(body)

    def ExpressionStatement(self):
        '''
        ExpressionStatement
            : Expression ';'
            ;
        '''
        expression = self.Expression()
        self._eat(';')

        return factory.ExpressionStatement(expression)

    def Expression(self):
        '''
            Expression
                : Literal
                ;
        '''
        return self.AdditiveExpression()

    def AdditiveExpression(self):

        ''' AdditiveExpression
            : Literal
            | AdditiveExpression ADDITIVE_OPERATOR Literal -> Literal ADDITIVE_OPERATOR Literal ADDITIVE_OPERATOR
            ;
        '''

        # try
        # 1
        # 1 + 4
        # 2 * 2 + 3 
        # NOTE: at this point in the parser code progress,
        # we try to consume as many multiplicative expressions before adding because of their higher precedence.
        left = self.MultiplicativeExpression()
        right = None

        while self._lookahead["type"] == "ADDITIVE_OPERATOR":
            operator = self._eat("ADDITIVE_OPERATOR")["value"]
            right = self.MultiplicativeExpression()

            left = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": left,
                "right": right
            }

        return left;

    def MultiplicativeExpression(self):

        left = self.PrimaryExpression()

        right = None

        while self._lookahead["type"] == "MULTIPLICATIVE_OPERATOR":
            operator = self._eat("MULTIPLICATIVE_OPERATOR")["value"]
            right = self.PrimaryExpression()
            left = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": left,
                "right": right
            }

        return left;

    def ParenthesizedExpression(self):

        left = self.PrimaryExpression()

        right = None

        while self._lookahead["type"] == "PARENTHESIS_OPERATOR":
            operator = self._eat("PARENTHESIS_OPERATOR")["value"]
            right = self.PrimaryExpression()
            left = {
                "type": "BinaryExpression",
                "operator": operator,
                "left": left,
                "right": right
            }

        return left;


    def PrimaryExpression(self):
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
        value = token["value"][1:-1]
        return factory.StringLiteral(value)

    def NumericLiteral(self):
        '''
        NumericLiteral
            : Number
            ;
        '''
        token = self._eat('NUMBER')
        value = int(token['value'])

        return factory.NumericLiteral(value)
