from repository import patterns

DEFAULT = """from random import randint

a = randint(0, 100)
print(a)
"""


def find_pattern(testcase):
    for prog in patterns:
        if prog.parse(testcase):
            return prog
    return None


# Simplest strategy.
# Find first pattern that match.
def generate(testcase):
    prog = find_pattern(testcase)

    if prog is None:
        return DEFAULT
    else:
        return prog.generate()
