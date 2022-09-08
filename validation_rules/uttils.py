import random


def random_swap(item1, item2, proba=0.1):
    if random.random() < proba:
        return item1, item2
    return item2, item1
    