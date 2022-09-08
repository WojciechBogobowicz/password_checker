import random
import string

SPECIAL_CHARACTERS = "".join([" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~",'"'])


def random_swap(item1, item2, proba=0.1):
    if random.random() < proba:
        return item1, item2
    return item2, item1

def genrate_random_password(
        length: int, 
        with_lowercase: bool = True,
        with_uppercase: bool = True,
        with_digits: bool = True,
        with_specialcharacters: bool = True
    ):
    base_characters = ''.join([
        string.ascii_lowercase if with_lowercase else '',
        string.ascii_uppercase if with_uppercase else '',
        string.digits if with_digits else '',
        SPECIAL_CHARACTERS if with_specialcharacters else ''
    ])
    return ''.join([random.choice(base_characters) for _ in range(length)])
