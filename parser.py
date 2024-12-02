class Parser():

    def parse(self, string):
        self._string = string
        return self.Program();

    def Program(self):
        '''
        main entry point
        Program
            : NumericLiteral
            ;
        '''
        return self.NumericLiteral()

    def NumericLiteral(self):
        '''
        NumericLiteral
            : Number
            ;
        '''
        return {
            "type": "NumericLiteral",
            "value": int(self._string)
        }
