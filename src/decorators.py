from functools import wraps


def log(filename=None):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write("my function OK")
                return result
            except Exception as e:
                if filename is not None:
                    with open(filename, "w") as file:
                        file.write(f"my function error:{e}. Input: {args, kwargs}")
                return func(*args, **kwargs)

        return wrapper

    return my_decorator


@log("mylog.txt")
def my_function(x, y):
    return x / y
