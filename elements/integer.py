from elements.elements import AbstractElement, PREFERRED_NAMES
from parser import Parser, ParserError
from utils import fix_return_string, rec_elements


class Integer(AbstractElement):
    PREFERRED_NAMES = PREFERRED_NAMES

    def __init__(self):
        self._min = float('inf')
        self._max = float('-inf')
        self._last_value = None
        self.name = None

    def parse(self, testcase: Parser):
        # Read next token
        try:
            value = testcase.token()
        except ParserError:
            return False

        # Convert into integer
        try:
            value = int(value)
        except ValueError:
            return False

        self._min = min(self._min, value)
        self._max = max(self._max, value)
        self._last_value = value
        return True

    @fix_return_string
    def generate(self):
        return """
        {name} = randint({min}, {max})
        print({name})
        """.format(name=self.name, min=self._min, max=self._max)

    @rec_elements
    def elements(self):
        return []
