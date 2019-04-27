from repository import patterns

DEFAULT = """from random import randint

a = randint(0, 100)
print(a)
"""


# Simplest strategy.
# Find first pattern that match.
def generate(testcases):
    for prog in patterns:
        if prog.parse(testcases):
            return prog.generate()

    return DEFAULT
