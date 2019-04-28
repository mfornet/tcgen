from codeforces.correct_test import test_problems
from codeforces.tools import get_problem
from generate import find_pattern


def run():
    problem, tc = get_problem("839E.html")

    print("name:", problem)
    for xtc in tc:
        print(xtc)

    gen = find_pattern(tc)

    if gen is None:
        print("Pattern not found!")

    else:
        print("pattern:", gen.__name__)
        print(gen.generate())


if __name__ == '__main__':
    assert test_problems()
    run()
