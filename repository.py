from elements import Integer, List, Integers
from language import code

patterns = []


def register(builder):
    """
    Convert pattern builder into compiled pattern.
    Keep __name__.
    """
    global patterns
    pattern = code()
    builder(pattern)
    prog = pattern.compile()
    prog.__name__ = builder.__name__
    patterns.append(prog)


@register
def one_int(pattern):
    pattern.add(Integer())


@register
def two_int(pattern):
    pattern.add(Integer())
    pattern.add(Integer())


@register
def simple_list(pattern):
    a = pattern.add(Integer())
    pattern.add(List(a, Integer()))


@register
def list_head_2_body_3(pattern):
    a = pattern.add(Integers(2))
    pattern.add(List(a[0], Integers(3)))
