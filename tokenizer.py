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

        string = self._string[self._cursor:]

        # parse Number
        if string[self._cursor].isdigit():

            number = ''
            while self._cursor < len(string) and string[self._cursor].isdigit():
                print('string: ', string, self._cursor)
                number += string[self._cursor]
                self._cursor += 1

            return {
                "type": 'NUMBER',
                "value": int(number)
            }

        # parse String
        if string[0] == '"':

            s = ''
            s += self._string[self._cursor]
            self._cursor += 1

            while self._string[self._cursor] != '"' and not self.isEOF():
                s += self._string[self._cursor]
                self._cursor += 1

            s += self._string[self._cursor]
            self._cursor += 1

            print("VALUE: ", s)
            return {
                "type": 'STRING',
                "value": s

            }
