__all__ = (
    'external_function',
    'some_important_fn',
)


def external_function(c):
    return c * 2


def some_important_fn(a, b):
    total = a + b
    result = external_function(total)
    return result
