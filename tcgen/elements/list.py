from elements.elements import AbstractElement
from elements.integer import Integer, Operation, get_value
from parser import Parser
from utils import fix_return_string, fix_string, indent, rec_elements


class List(AbstractElement):
    PREFERRED_NAMES = ['l'] + Integer.PREFERRED_NAMES

    def __init__(self, total, elem=None):
        if elem is None:
            elem = Integer()

        assert isinstance(total, int) or isinstance(total, Integer) or isinstance(total, Operation)

        self._total = total
        self._token = elem
        self.name = None

    def _upper_limit(self):
        return get_value(self._total)

    def _gen_total(self):
        if isinstance(self._total, int):
            return self._total
        else:
            return self._total.name

    def parse(self, testcase: Parser):
        for i in range(self._upper_limit()):
            if not self._token.parse(testcase):
                return False
        return True

    @fix_return_string
    def generate(self):
        code = fix_string("""
        for _ in range({total}):
        """.format(total=self._gen_total())) + '\n' + indent(self._token.generate(), +1)
        return code

    @rec_elements
    def elements(self):
        yield self._token
