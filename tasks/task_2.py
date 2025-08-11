from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print("Из кэша")
            return cache[key]
        cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper
