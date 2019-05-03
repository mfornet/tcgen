import argparse
from os import listdir
from os.path import join

from .generate import generate


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--version', action='store_true', default=False)
    parser.add_argument('-p', '--path', dest='path', default=None)
    parser.add_argument('-o', '--output', dest='output', default=None)
    parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()


def get_testcases(args):
    if args.path is not None:
        testcases = []

        for fl in listdir(args.path):
            if fl.endswith('.in'):
                with open(join(args.path, fl)) as f:
                    testcases.append(f.read())

        if args.verbose:
            print("Loaded {} testcases.".format(len(testcases)))

        return testcases
    else:
        print("Provide testcases path using --path")
        exit(1)


def run(args):
    testcases = get_testcases(args)
    code = generate(testcases)

    if args.output is None:
        print(code)
    else:
        with open(args.output, 'w') as f:
            f.write(code)


if __name__ == '__main__':
    args = get_args()

    if args.version:
        from ._version import VERSION
        print(VERSION)
        exit(0)

    run(args)
