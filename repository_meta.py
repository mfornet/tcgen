from functools import partial

import repository
from language import code

VERBOSE = False


def register(builder):
    """
    Convert pattern builder into compiled pattern.
    Keep __name__.
    """

    if VERBOSE:
        print("Register:", builder.__name__)

    def lazy():
        pattern = code()
        builder(pattern)
        prog = pattern.compile()
        prog.__name__ = builder.__name__
        return prog

    repository.PATTERNS.append(lazy)


def dict_get(dic, key, default):
    if key in dic:
        return dic[key]
    else:
        return default()


def get_interval(interval_str, name_dict):
    # Try to parse as int
    if '..' not in interval_str:
        lower = int(interval_str)
        upper = lower + 1
        return lower, upper

    lower, upper = interval_str.split('..')
    add = upper.startswith('=')
    if add: upper = upper[1:]

    lower = dict_get(name_dict, lower, partial(int, lower))
    upper = dict_get(name_dict, upper, partial(int, upper))

    if add: upper += 1

    return lower, upper


def generate(ordered_params, params_idx, name_dict):
    if params_idx == len(ordered_params):
        yield name_dict

    else:
        name, value = ordered_params[params_idx]
        lower, upper = get_interval(value, name_dict)

        for v in range(lower, upper):
            name_dict[name] = v

            for param_variants in generate(ordered_params, params_idx + 1, name_dict):
                yield param_variants

        if name in name_dict:
            del name_dict[name]


def generate_all(ordered_params):
    name_dict = {}
    return generate(ordered_params, 0, name_dict)


def register_all(**params):
    ordered_params = list(params.items())

    def proc(func):
        for param_variants in generate_all(ordered_params):
            new_func = partial(func, **param_variants)
            new_func.__name__ = func.__doc__.format(**param_variants).strip("\t\n ")
            register(new_func)

    return proc


# def f(**kwargs):
#     kwargs = list(kwargs.items())
#     for x in generate_all(kwargs):
#         print(x)
#
#
# if __name__ == '__main__':
#     f(b='0..3', a="0..=b", c="2..4")
#     f(b='2')
