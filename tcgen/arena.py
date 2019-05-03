from elements import List, Integer, Compound, Integers, String
from language import code

# Build pattern
pattern = code()
a = Integers(3)
b = Integer()
n = a[1]
pattern.add(a)
pattern.add(List(n, b))

prog = pattern.compile()

# Build testcases
# ['\n2 1 4\n8\n', '3 2 5\n1\n4\n']
testcases = """
2 1 4
8
-
3 2 5
1
4
"""

tc = testcases.split('-\n')

# Parse program
prog.parse(tc)

assert prog.ok

print(prog.generate())
exit(0)

# Print test
print("""@example
def TESTNAME(self, pattern):
    

    return dict(
        testcases={},
        expected={}
    )""".format(repr(tc), repr(prog.generate())))
# print(repr(prog.generate()))
