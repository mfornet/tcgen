import random
from os import listdir
from os.path import join

import bs4

CODEFORCES_PROBLEMS = '.'


def parse_testcase(name):
    with open(join(CODEFORCES_PROBLEMS, name)) as f:
        html = f.read()

    soup = bs4.BeautifulSoup(html, features="html5lib")
    sample_test = soup.find("div", {"class": "sample-tests"})

    tc = []

    for node_inp in sample_test.find_all("div", {"class": "input"}):
        content = node_inp.find("pre")
        content = str(content)
        content = content[5:-6]
        content = content.replace('<br/>', '\n')
        tc.append(content)

    return tc


def codeforces_problems():
    return listdir(CODEFORCES_PROBLEMS)


def random_problem():
    probs = codeforces_problems()
    prob = random.choice(probs)
    tc = parse_testcase(prob)
    return prob, tc


def get_problem(name=None):
    if name is None:
        prob, tc = random_problem()
    else:
        tc = parse_testcase(name)
        prob = name
    return prob, tc


if __name__ == '__main__':
    print(random_problem())
