from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def decorator(func):
        @wraps(func)
        def strip(*args, **kwargs):
            text = func(*args, **kwargs)
            s = max(0, start)
            e = min(len(text), end)
            return text[:s] + DOT * (e - s) + text[e:]
        return strip      
    return decorator

def tester(x,y,text):
    @strip_range(x,y)
    def gen_output(text):
        return text
    actual = gen_output(text=text)
    return actual
