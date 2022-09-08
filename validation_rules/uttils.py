import random
import string

SPECIAL_CHARACTERS = "".join([" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~",'"'])


def random_swap(item1, item2, proba=0.1):
    if random.random() < proba:
        return item1, item2
    return item2, item1
    