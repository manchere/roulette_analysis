import numpy as np
from collections import Counter, Iterable
from statistics import mode, mean


def get_most_frequent(lst):
    return np.bincount(lst).argmax()


def get_n_most_frequent(lst, n):
    return Counter(lst).most_common(n)


def get_frequency_of(value, lst, start=0, end=None):
    return lst[start:end].count(value)
