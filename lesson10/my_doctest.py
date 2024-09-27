def my_fancy_function(a, b):
    """
    This function calculates a + b
    >>> my_fancy_function(1, 2)
    4
    """
    return a + b + 1


def hello():
    """
    >>> raise ValueError(1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 1
    """
    pass


def calculate_triangle_area(a, b, c):
    """
    I expect area of triangle will be calculated
    >>> calculate_triangle_area(10, 15, 10)
    49.607837082461074
    """
    p = (a + b + c) / 2.
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5