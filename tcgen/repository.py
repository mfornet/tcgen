from .elements import List, Integers, String, Integer
from .repository_meta import register_all
from ._pattern import PATTERNS


@register_all(head="1..=5")
def integers(head):
    yield Integers(head)


@register_all(head="1..=3", index="0..head", body="1..=5")
def list_head_index_body(head, index, body):
    h = Integers(head)
    yield h
    yield List(h[index], Integers(body))


@register_all(block0="1..4", block1="1..4")
def two_blocks_reversed_index(block0, block1):
    h = Integers(2)
    yield h
    yield List(h[1], Integers(block0))
    yield List(h[0], Integers(block1))


@register_all(block_int="1..4")
def two_blocks_string_integer(block_int):
    h = Integers(2)
    yield h
    yield List(h[0], String())
    yield List(h[1], Integers(block_int))


@register_all(head="1..=3", index="0..head")
def list_head_string(head, index):
    h = Integers(head)
    yield h
    yield List(h[index], String())


@register_all(head="1..3")
def board_square(head):
    h = Integers(head)
    yield h
    yield List(h[0], List(h[0], Integer()))


@register_all(head="2..=4")
def board_rectangle(head):
    h = Integers(head)
    yield h
    yield List(h[0], List(h[1], Integer()))
