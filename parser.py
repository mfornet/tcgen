class Parser:
    BLANK = ' \n\t'

    def __init__(self, text):
        self._text = text
        self._pointer = 0

    def peek(self):
        if self._pointer == len(self._text):
            return None
        else:
            return self._text[self._pointer]

    def get(self):
        c = self.peek()
        if c is not None:
            self._pointer += 1
        return c

    @staticmethod
    def is_readable(ch):
        return ch is not None and ch not in Parser.BLANK

    def token(self, allow_blank=True):
        if allow_blank:
            if self.peek() is None:
                raise ParserError("Token expected found blank char.")

            while not self.is_readable(self.peek()):
                self.get()
        else:
            if not self.is_readable(self.peek()):
                raise ParserError("Token expected found blank char.")

        token = ""

        while True:
            if not self.is_readable(self.peek()):
                break
            token += self.get()

        return token

    def consume_blank(self):
        while True:
            x = self.peek()
            if x is not None and x in Parser.BLANK:
                self.get()
            else:
                break


class ParserError(BaseException):
    pass
