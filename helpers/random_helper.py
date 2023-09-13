import random

ru_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_lowercase = 'abcdefghijklmnopqrstuvwxyz'
en_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuations = r"""!"#$%&'()*+,-—–./:;<=>?@[\]^_`{|}~№«»“”„‹›‘’‚"""
whitespaces = ' \t\n\r\v\f'


def random_small_side():
    """Generate random side between 1 and 10"""

    return random.randint(1, 10)


def random_big_side():
    """Generate random side between 10 and 100"""

    return random.randint(10, 100)


def random_triangle_side():
    """Generate random isosceles triangle side"""

    return random.choice([random_small_side(), random_big_side()])


def random_lower_letters():
    """Generate random ru and en letters"""

    letters = ru_lowercase + en_lowercase + ru_uppercase + en_uppercase
    return ''.join(random.choice(letters) for _ in range(10))


def random_punctuations():
    """Generate random punctuations"""

    return ''.join(random.choice(punctuations) for _ in range(10))


def random_whitespaces():
    """Generate random whitespaces"""

    return ''.join(random.choice(whitespaces) for _ in range(10))


def random_bool():
    """Generate random bool param"""

    return random.choice([True, False])
