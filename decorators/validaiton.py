from functools import wraps


def int_args(func):
    @wraps(func)
    def check(*args):
        if not all(isinstance(arg,(int)) for arg in args):
            raise TypeError
        elif any(arg < 0 for arg in args):
            raise ValueError  
        return func(*args)
    return check


@int_args
def check_type():
    return

print(check_type(1, 2.1, 3))
    