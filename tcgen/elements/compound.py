from .elements import AbstractElement
from ..parser import Parser
from ..utils import rec_elements


class Compound(AbstractElement):
    def __init__(self, elems):
        self._elems = elems

    def parse(self, testcase: Parser):
        for e in self._elems:
            if not e.parse(testcase):
                return False
        return True

    def generate(self):
        return '\n'.join(e.generate() for e in self._elems)

    @rec_elements
    def elements(self):
        return self._elems
