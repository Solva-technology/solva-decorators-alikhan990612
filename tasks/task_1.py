from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            print(f"Вызов: {func.__name__}{args}")
        if kwargs:
            print(f"Вызов: {func.__name__}{kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper
