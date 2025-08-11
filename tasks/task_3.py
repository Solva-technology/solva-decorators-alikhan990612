from functools import wraps


def validate_positive(func):
    MAX_VALUE = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, int | float) and value <= MAX_VALUE:
                raise ValueError("Все аргументы должны быть положительными")
        for value in kwargs.values():
            if isinstance(value, int | float) and value <= MAX_VALUE:
                raise ValueError("Все аргументы должны быть положительными")
        result = func(*args, **kwargs)
        return result
    return wrapper
