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

    ''' some probably unclear notes on how this parser achieves correct order of precidence (mult/div higher than add/sub):
    - the Additive/Multiplicative Primary Expression types control the flow of parsing.
    - the expression type with the lowest precidence is processed first, and in terms of more specific types
    - i.e. first step is processing expression as if it's additive. then inside that, process operands as if they
    are types w/ higher precidence, i.e. multiplicative, but they can also trivially be numeric literals.
    - if those sub exps are multiplicative, they get processed that way.  otherwise, the additive keeps associating
    left, building binary expressions. 
    '''
    def AdditiveExpression(self):

        ''' MultiplicativeExpression
            : Literal
            | MultiplicativeExpression ADDITIVE_OPERATOR MultiplicativeExpression -> MultiplicativeExpression ADDITIVE_OPERATOR MultiplicativeExpression
            ;
        '''

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

    def PrimaryExpression(self):
        '''
            Primary Expression
            : Literal
            | ParenthesizedExpression
            ;
        '''
        # this is how we achieve higher precidence when using parentheses.
        if self._lookahead["type"] == "(":
            return self.ParenthesizedExpression()

        return self.Literal()

    '''
        ParenthesizedExpression
        : '(' Expression ')'
        ;
    '''
    def ParenthesizedExpression(self):

        self._eat("(")
        expression = self.Expression();
        self._eat(")")
        return expression


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
