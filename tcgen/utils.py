from random import randint


def indent(code, size):
    final_eol = code.endswith('\n')
    if final_eol: code = code[:-1]
    lines = code.split('\n')
    lines = [' ' * (4 * size) + line for line in lines]
    code = '\n'.join(lines)
    if final_eol: code += '\n'
    return code


def fix_string(code):
    """
    Fix indentation and empty lines from string coming out of the function.
    """
    lines = code.split('\n')

    # Remove first line if empty
    if not lines[0]:
        lines = lines[1:]

    # Detect tabsize
    size = 0
    while lines[0][size] in ' ':
        size += 1

    lines = list(map(lambda l: l[size:], lines))

    if not lines[-1]:
        lines = lines[:-1]

    code = '\n'.join(lines)
    return code


def fix_return_string(func):
    """
    Decorator that fix the string resulting from a function.
    """

    def _func(*args):
        return fix_string(func(*args))

    return _func


def names(preferred_names):
    """
    Generator of names to feed variables
    """

    def random_word(length):
        return ''.join(map(lambda x: chr(x), [randint(97, 122) for _ in range(length)]))

    for x in preferred_names:
        yield x

    while True:
        name = random_word(3)
        yield name


def rec_elements(elem_iterator):
    def _func(*args):
        for elem in elem_iterator(*args):
            yield elem

            for sub_elem in elem.elements():
                yield sub_elem

    return _func


@rec_elements
def element_iterator(elements):
    return elements
