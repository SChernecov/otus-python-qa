import random


def random_small_side():
    """Generate random side between 10 and 100"""

    return random.randint(10, 100)


def random_big_side():
    """Generate random side between 1 and 10"""

    return random.randint(1, 10)


def random_triangle_side():
    """Generate random isosceles triangle side"""

    return random.choice([random_small_side(), random_big_side()])


def random_height():
    """Generate random height between 1 and 10"""

    return random.randint(1, 100)
