from functools import wraps


def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print("my func is OK")
                    return result
                else:
                    with open(filename, "w") as file:
                        file.write(f"my func is OK, result = {result}")
            except Exception as e:
                if filename is None:
                    print("my func is BAD")
                else:
                    with open(filename, "w") as file:
                        file.write(f"my func error: {e} ")

        return wrapper

    return my_decorator


@log("mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(1, 2))
