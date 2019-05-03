from elements.elements import AbstractElement
from elements.integer import Integer
from parser import Parser
from utils import fix_return_string, rec_elements


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
