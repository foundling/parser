import re

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

        if not self.hasMoreTokens():
            return None

        # match a number
        string = self._string[self._cursor:]
        matched = re.match('\d+', string)

        if matched:
            self._cursor += len(matched[0])
            return {
                "type": 'NUMBER',
                "value": int(matched[0])
            }

        # Match a string
        matched = re.match("'([^'].*?)'", string)

        if matched:
            self._cursor += len(matched[0])
            return {
                "type": 'STRING',
                "value": matched[0]
            }
