from elements import Integer, List, Integers, String
from language import code

patterns = []


def register(builder):
    """
    Convert pattern builder into compiled pattern.
    Keep __name__.
    """

    global patterns

    def lazy():
        pattern = code()
        builder(pattern)
        prog = pattern.compile()
        prog.__name__ = builder.__name__
        return prog

    patterns.append(lazy)


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


@register
def head_2_list_2_list_1(pattern):
    a = pattern.add(Integers(2))
    pattern.add(List(a[1], Integers(2)))
    pattern.add(List(a[0], Integer()))


@register
def head_2_list_string_list_3(pattern):
    a = pattern.add(Integers(2))
    pattern.add(List(a[0], String()))
    pattern.add(List(a[1], Integers(3)))
