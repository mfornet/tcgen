from elements.elements import AbstractElement, PREFERRED_NAMES
from parser import Parser, ParserError
from utils import fix_return_string


class String(AbstractElement):
    PREFERRED_NAMES = ['s', 'x', 'y', 'z'] + PREFERRED_NAMES

    def __init__(self):
        self._alpha = set()
        self._min_len = float('inf')
        self._max_len = float('-inf')
        self.name = None

    def parse(self, testcase: Parser):
        try:
            value = testcase.token()
        except ParserError:
            return False

        for x in value:
            self._alpha.add(x)

        self._min_len = min(self._min_len, len(value))
        self._max_len = max(self._max_len, len(value))
        return True

    @fix_return_string
    def generate(self):
        return """
        {name} = ''.join([choice("{alpha}") for _ in range(randint({min}, {max}))])
        print({name})
        """.format(name=self.name, alpha=''.join(sorted(self._alpha)), min=self._min_len, max=self._max_len)

    def elements(self):
        return []
