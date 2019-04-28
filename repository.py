from elements import List, Integers, String
from repository_meta import register_all

PATTERNS = []


@register_all(head="1..=5")
def integers(pattern, head):
    """
    integers({head})
    """
    pattern.add(Integers(head))


@register_all(head="1..=3", index="0..head", body="1..=5")
def list_head_index_body(pattern, head, index, body):
    """
    list_head_index_body({head},{index},{body})
    """
    a = pattern.add(Integers(head))
    pattern.add(List(a[index], Integers(body)))


@register_all(block0="1..4", block1="1..4")
def two_blocks_reversed_index(pattern, block0, block1):
    """
    two_blocks_reversed_index({block0},{block1})
    """
    a = pattern.add(Integers(2))
    pattern.add(List(a[1], Integers(block0)))
    pattern.add(List(a[0], Integers(block1)))


@register_all(block_int="1..4")
def two_blocks_string_integer(pattern, block_int):
    """
    two_blocks_string_integer({block_int})
    """
    a = pattern.add(Integers(2))
    pattern.add(List(a[0], String()))
    pattern.add(List(a[1], Integers(block_int)))
