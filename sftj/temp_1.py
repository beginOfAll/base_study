import time
from functools import wraps
import random


def time_it(func):
    @wraps(func)
    def w_fun(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('s:', (t2 - t1))
        return res

    return w_fun


@time_it
def find1(l, t):
    for idx, v in enumerate(l):
        if v == t:
            return idx
    return None


@time_it
def find2(l, t):
    for i in range(len(l)):
        if l[i] == t:
            return i
    return None


@time_it
def find3(l, t):
    low = 0
    high = len(l) - 1
    while high >= low:
        mid = (low + high) // 2
        g = l[mid]
        if g == t:
            return mid
        elif g > t:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    s_list = [str(i) for i in range(100000)]
    random.shuffle(s_list)
    target = "99999"
    print(find1(s_list, target))
    print(find2(s_list, target))
    print(find3(s_list, target))
