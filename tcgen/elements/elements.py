from ..parser import Parser

PREFERRED_NAMES = ['n', 'm', 'k', 'a', 'b', 'c', 'd', 't', 'q']


class AbstractElement:

    def parse(self, testcase: Parser):
        raise NotImplementedError()

    def generate(self):
        raise NotImplementedError()

    def elements(self):
        raise NotImplementedError()
