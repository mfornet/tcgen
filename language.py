from elements import AbstractElement
from parser import Parser
from utils import names, element_iterator


class Code:
    def __init__(self):
        self._elements = []

    def add(self, elem: AbstractElement):
        self._elements.append(elem)
        return elem

    def assign_names(self):
        # assign names to every element that needs it
        used_names = set()

        for elem in element_iterator(self._elements):
            if hasattr(elem, 'name'):
                if elem.name is not None:
                    if elem.name in used_names:
                        # Name was previously used
                        elem.name = None
                    else:
                        used_names.add(elem.name)

        for elem in element_iterator(self._elements):
            if hasattr(elem, 'name'):
                if elem.name is None:
                    for pref_name in names(elem.PREFERRED_NAMES):
                        if pref_name not in used_names:
                            used_names.add(pref_name)
                            elem.name = pref_name
                            break

    def compile(self):
        self.assign_names()
        return Program(self._elements)


class Program:
    def __init__(self, elements):
        self._elements = elements
        self._testcases = None
        self._ok = True

    @property
    def ok(self):
        return self._ok

    def _parse(self, tc):
        tc = Parser(tc)

        for elem in self._elements:
            self._ok = elem.parse(tc)

            # Break parsing since it failed parsing object `elem`
            if not self._ok:
                return

        tc.consume_blank()
        self._ok = tc.peek() is None

    def parse(self, testcases):
        self._testcases = testcases

        for tc in testcases:
            self._parse(tc)

            if not self.ok:
                return False

        return True

    @property
    def header(self):
        return "from random import randint\n"

    def generate(self):

        body = '\n\n'.join(
            obj.generate() for obj in self._elements
        ) + '\n'

        code = self.header + '\n' + body
        return code


code = Code
