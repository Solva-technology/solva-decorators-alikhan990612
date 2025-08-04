from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Из кэша")
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return wrapper
