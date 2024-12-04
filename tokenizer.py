import re

spec = [

    # Whitespace
    ['\s+', None],

    # Numbers
    ['\d+','NUMBER'],

    # Strings
    ["'[^']*'",'STRING'],
    ['"[^"]*"','STRING']

]

class Tokenizer():

    def __init__(self):
        self._string = '' 
        self._cursor = 0

    def init(self, string):
        self._string = string

    def isEOF(self):
        return self._cursor == len(self._string)

    def hasMoreTokens(self):
        return self._cursor < len(self._string)

    def getNextToken(self):

        #import pdb; pdb.set_trace()
        if not self.hasMoreTokens():
            print('no more tokens')
            return None

        string = self._string[self._cursor:]

        for regexp, token_type in spec:

            matched_token = self._match(regexp, string)  

            # this token type didn't match, keep looking
            if matched_token is None:
                continue

            # it's whitespace, ignore
            if matched_token and token_type is None:
                print('ignoring whitespace')
                return self.getNextToken()

            return {
                "type": token_type,
                "value": matched_token
            }
        
        raise SyntaxError(f"Unexpected Token: {string[0]}") 

    def _match(self, regexp, string):

        matched = re.match(regexp, string)

        if matched:
            self._cursor += len(matched[0])
            return matched[0]
        else:
            return None

