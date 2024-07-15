import numpy as np
from collections import Counter, Iterable
from operator import itemgetter
from statistics import mode, mean



def get_most_frequent(lst):
    return np.bincount(lst).argmax()


def get_n_most_frequent(lst, n, rate=True):
    lst = Counter(lst).most_common(n)
    if not rate:
        return list(map(itemgetter(0), lst))
    return lst


def get_n_least_frequent(lst, n, rate=True):
    lst = list(reversed(Counter(lst).most_common()[-n:]))
    if not rate:
        return map(itemgetter(0), lst)
    return lst


def get_frequency_of(value, lst, start=0, end=None):
    return lst[start:end].count(value)


def get_diff_of_arr(lst1, lst2):

    return np.setdiff1d(list(map(lambda x: x, lst1)),
                        list(map(lambda y: y, lst2)))

