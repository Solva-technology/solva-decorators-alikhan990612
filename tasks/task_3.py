from functools import wraps


def validate_positive(func):
    MAX_VALUE = 0

    @wraps(func)
    def wrapper(*args):
        for values in args:
            if values <= MAX_VALUE:
                raise ValueError("Все аргументы должны быть положительными")
        result = func(*args)
        return result
    return wrapper
