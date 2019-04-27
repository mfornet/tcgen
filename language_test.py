import unittest

from elements import Integer, List, Integers, Compound, String
from language import code
from parser import Parser, ParserError


def example(test_example):
    def extended_test_example(self):
        pattern = code()
        config = test_example(self, pattern)
        prog = pattern.compile()
        prog.parse(config.get("testcases"))

        if not config.get("should_fail", False):
            self.assertTrue(prog.ok)
            self.assertEqual(prog.generate(), config.get("expected"))
        else:
            self.assertFalse(prog.ok)

    return extended_test_example


class TestLanguageBehavior(unittest.TestCase):
    @example
    def test_one_integer(self, pattern):
        pattern.add(Integer())

        return dict(
            testcases=["1\n", "2\n", "100\n"],
            expected="from random import randint, choice\n\nn = randint(1, 100)\nprint(n)\n",
        )

    @example
    def test_two_integers(self, pattern):
        pattern.add(Integer())
        pattern.add(Integer())

        return dict(
            testcases=["1 3\n", "2 1\n", "100\n2\n"],
            expected='from random import randint, choice\n\nn = randint(1, 100)\nprint(n)\n\n'
                     'm = randint(1, 3)\nprint(m)\n'
        )

    @example
    def test_fixed_two(self, pattern):
        pattern.add(Integers(2))

        return dict(
            testcases=["1 4\n", "2 2\n", "100 -2\n"],
            expected='from random import randint, choice\n\nn, m = randint(1, 100), randint(-2, 4)\nprint(n, m)\n'
        )

    @example
    def test_fail_one_integer(self, pattern):
        pattern.add(Integer())

        return dict(
            testcases=["1 3\n", "2 1\n", "100 2\n"],
            should_fail=True,
        )

    @example
    def test_list(self, pattern):
        f = Integers(2)
        pattern.add(List(3, f))

        return dict(
            testcases=["1 4\n2 2\n3 3\n", "2 2\n1 5\n-1 2\n"],
            expected='from random import randint, choice\n\nfor _ in range(3):'
                     '\n    n, m = randint(-1, 3), randint(2, 5)\n    print(n, m)\n'
        )

    @example
    def test_list_parametric(self, pattern):
        a = pattern.add(Integer())
        pattern.add(List(a, Integers(2)))

        return dict(
            testcases=['\n1\n2 3\n', '3\n1 2\n2 3\n4 5\n'],
            expected='from random import randint, choice\n\nn = randint(1, 3)\nprint(n)\n\n'
                     'for _ in range(n):\n    m, k = randint(1, 4), randint(2, 5)\n    print(m, k)\n'
        )

    @example
    def test_list_parameter_in_fixed(self, pattern):
        a = Integers(3)
        b = Integer()
        n = a[1]
        pattern.add(a)
        pattern.add(List(n, b))

        return dict(
            testcases=['\n2 1 4\n8\n', '3 2 5\n1\n4\n'],
            expected='from random import randint, choice\n\nn, m, k = randint(2, 3), randint(1, 2), randint(4, 5)\n'
                     'print(n, m, k)\n\nfor _ in range(m):\n    a = randint(1, 8)\n    print(a)\n'
        )

    @example
    def test_compound(self, pattern):
        t = Integer()
        n = Integer()
        l = List(n, Integer())
        f = List(t, Compound([n, l]))
        pattern.add(t)
        pattern.add(f)

        return dict(
            testcases=['\n2\n3\n1 2 3\n4\n1 2 3 4\n', '1\n5\n1 2 3 4 5\n'],
            expected='from random import randint, choice\n\nn = randint(1, 2)\nprint(n)\n\n'
                     'for _ in range(n):\n    m = randint(3, 5)\n    print(m)\n    for _ in range(m):\n'
                     '        a = randint(1, 5)\n        print(a)\n'
        )

    @example
    def test_string(self, pattern):
        pattern.add(String())

        return dict(
            testcases=['\nxyaz\n', 'verde\n'],
            expected='from random import randint, choice\n\n'
                     's = \'\'.join([choice("adervxyz") for _ in range(randint(4, 5))])\nprint(s)\n'
        )


class TestParser(unittest.TestCase):
    def test_parser_basics(self):
        p = Parser("hoy no es el dia!")
        self.assertEqual(p.peek(), 'h')
        self.assertEqual(p.token(), 'hoy')
        self.assertEqual(p.get(), ' ')
        self.assertEqual(p.get(), 'n')
        self.assertEqual(p.token(), 'o')

        with self.assertRaises(ParserError):
            p.token(allow_blank=False)

        for s in "es el dia!".split():
            self.assertEqual(p.token(), s)

        self.assertEqual(p.get(), None)

        with self.assertRaises(ParserError):
            p.token()

    def test_end(self):
        p = Parser("this is a token")
        p._pointer = 14
        token = p.token()
        self.assertEqual(token, "n")


if __name__ == '__main__':
    unittest.main()
