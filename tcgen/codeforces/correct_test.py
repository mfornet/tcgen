import json
import unittest

from codeforces.tools import get_problem
from generate import find_pattern


def check(prob, pattern_name, with_assert=None):
    _, tc = get_problem(prob)
    gen = find_pattern(tc)

    if with_assert is not None:
        with_assert.assertIsNotNone(gen, "problem {} expected {}".format(prob, pattern_name))
        with_assert.assertEqual(gen.__name__, pattern_name)
        return True
    else:
        if gen is None: return False
        return gen.__name__ == pattern_name


def test_problems(with_assert=None):
    with open('ok.json') as f:
        data = json.load(f)

    for prob, pattern_name in data.items():
        if not check(prob, pattern_name, with_assert):
            return False

    return True


class TestCodeforces(unittest.TestCase):
    def test_problems(self):
        test_problems(self)


if __name__ == '__main__':
    unittest.main()
