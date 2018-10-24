import time
from sftj.temp_1 import time_it
import random


# 递归求和list
@time_it
def list_sum1(l):
    if len(l) > 1:
        return l[0] + list_sum1(l[1:])
    elif len(l) == 1:
        return l[0]
    else:
        return 0


@time_it
def list_sum2(l):
    r = 0
    for i in l:
        r += i
    return r


# 快速排序
@time_it
def qsort(l):
    if len(l) > 1:
        s = random.randint(0, len(l) - 1)
        l.remove(l[s])
        left = [i for i in l if i < s]
        right = [i for i in l if i >= s]
        # return qsort(left).extend(right)
        t = qsort(left)
        t.append(s)
        t.extend(qsort(right))
        return t

    else:
        return l


@time_it
def qsort2(l):
    if len(l) > 1:
        s = l[0]
        left = [i for i in l[1:] if i < s]
        right = [i for i in l[1:] if i >= s]
        # return qsort(left).extend(right)
        t = qsort(left)
        t.append(s)
        t.extend(qsort(right))
        return t

    else:
        return l


if __name__ == '__main__':
    l = [99999, 77777, 33333, 22222, 709, 50, 30, 5, 0, -22, -999, ]
    t1 = time.time()
    r = qsort(l)
    print('z', time.time() - t1)
    print(r)
