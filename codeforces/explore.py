from tqdm import tqdm, TqdmLogger as logger

from codeforces.tools import codeforces_problems, get_problem
from generate import find_pattern


class Tabular:
    def __init__(self):
        self._dic = {}

    def add(self, name):
        self._dic[name] = self._dic.get(name, 0) + 1

    def report(self):
        L = [(v, k) for k, v in self._dic.items()]
        L.sort(reverse=True)
        print()
        for v, k in L:
            print("{:<8} {}".format(v, k))


def explore():
    total = 0
    ok = 0

    tab = Tabular()

    for idx, prob in tqdm(enumerate(codeforces_problems())):
        try:
            p, tc = get_problem(prob)
            pat = find_pattern(tc)

            total += 1

            if pat is not None:
                tab.add(pat.__name__)
                ok += 1
                logger.log("{}/{}".format(ok, total))
        except:
            print("Fail on problem: {}".format(prob))

        if (idx + 1) % 100 == 0:
            tab.report()

    tab.report()


if __name__ == '__main__':
    # print(codeforces_problems()[533])
    explore()
