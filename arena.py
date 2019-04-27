from elements import List, Integer, Compound
from language import code

# Build pattern
pattern = code()
t = Integer()
n = Integer()
l = List(n, Integer())
f = List(t, Compound([n, l]))
pattern.add(t)
pattern.add(f)

prog = pattern.compile()

# Build testcases
testcases = """
2
3
1 2 3
4
1 2 3 4
-
1
5
1 2 3 4 5
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
