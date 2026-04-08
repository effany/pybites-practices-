from functools import wraps


def make_html(element):                # Layer 1: takes the argument ("p", "b", etc.)
    def decorator(func):               # Layer 2: takes the function
        @wraps(func)
        def wrapped(*args, **kwargs):  # Layer 3: the wrapper
            result = func(*args, **kwargs)
            return f"<{element}>{result}</{element}>"
        return wrapped
    return decorator


@make_html("p")
@make_html("b")
def greet(name):
    return f"Hi {name}"


print(greet("World"))