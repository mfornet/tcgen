from elements import List, Integer, Compound, Integers, String
from language import code

# Build pattern
pattern = code()
pattern.add(String())

prog = pattern.compile()

# Build testcases
testcases = """
xyaz
-
verde
"""

tc = testcases.split('-\n')

# Parse program
prog.parse(tc)

assert prog.ok

# print(prog.generate())
# exit(0)

# Print test
print("""@example
def TESTNAME(self, pattern):
    

    return dict(
        testcases={},
        expected={}
    )""".format(repr(tc), repr(prog.generate())))
# print(repr(prog.generate()))
