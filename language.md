# Language description

```python
from tcgen.language import code

t = code.create()

header = t.fixed(1)
t.list(header[0])

prog = t.compile()

testcases = [
    "2\n1 2\n",
    "3\n1 2 3\n",
]

for tc in testcases:
    prog.feed(tc)

assert prog.ok()
print("confidence:", prog.confidence())
print(prog.generate())
```