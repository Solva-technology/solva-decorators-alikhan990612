from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args):
        print(f"Вызов: {func.__name__}{args}")
        result = func(*args)
        print(f"Результат: {result}")
        return result
    return wrapper
