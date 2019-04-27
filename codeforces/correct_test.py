import json
import unittest

from codeforces.tools import get_problem
from generate import find_pattern


def check(prob, pattern_name):
    _, tc = get_problem(prob)
    gen = find_pattern(tc)
    return gen.__name__ == pattern_name


def test_problems():
    with open('ok.json') as f:
        data = json.load(f)

    for prob, pattern_name in data.items():
        if not check(prob, pattern_name):
            return False

    return True


class TestCodeforces(unittest.TestCase):
    def test_problems(self):
        self.assertTrue(test_problems())


if __name__ == '__main__':
    unittest.main()
