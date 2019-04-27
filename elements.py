from parser import Parser, ParserError
from utils import fix_return_string, fix_string, indent, rec_elements

PREFERRED_NAMES = ['n', 'm', 'k', 'a', 'b', 'c', 'd', 't', 'q']


class AbstractElement:

    def parse(self, testcase: Parser):
        raise NotImplementedError()

    def generate(self):
        raise NotImplementedError()

    def elements(self):
        raise NotImplementedError()


class Integer(AbstractElement):
    PREFERRED_NAMES = PREFERRED_NAMES

    def __init__(self):
        self._min = float('inf')
        self._max = float('-inf')
        self._last_value = None
        self.name = None

    def parse(self, testcase: Parser):
        try:
            value = testcase.token()
            value = int(value)
            self._min = min(self._min, value)
            self._max = max(self._max, value)
            self._last_value = value
            return True
        except ParserError:
            return False

    @fix_return_string
    def generate(self):
        return """
        {name} = randint({min}, {max})
        print({name})
        """.format(name=self.name, min=self._min, max=self._max)

    @rec_elements
    def elements(self):
        return []


class Integers(AbstractElement):
    def __init__(self, total):
        self._total = total
        self._tokens = [Integer() for _ in range(total)]

    def parse(self, testcase: Parser):
        for token in self._tokens:
            if not token.parse(testcase):
                return False
        return True

    @fix_return_string
    def generate(self):
        variables = ', '.join(tok.name for tok in self._tokens)
        gen = ', '.join('randint({min}, {max})'.format(min=tok._min, max=tok._max) for tok in self._tokens)

        return """
        {variables} = {gen}
        print({variables})
        """.format(variables=variables, gen=gen)

    @rec_elements
    def elements(self):
        return self._tokens

    def __getitem__(self, idx):
        return self._tokens[idx]


# TODO: List of any element type (other list or fixed values)
class List(AbstractElement):
    PREFERRED_NAMES = ['l'] + Integer.PREFERRED_NAMES

    def __init__(self, total, elem=None):
        if elem is None:
            elem = Integer()

        assert isinstance(total, int) or isinstance(total, Integer)

        self._total = total
        self._token = elem
        self.name = None

    def _upper_limit(self):
        if isinstance(self._total, int):
            return self._total
        else:
            return self._total._last_value

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
