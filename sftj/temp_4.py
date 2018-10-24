import queue
from collections import OrderedDict

goods = {}
goods['乐谱'] = {
    '唱片': 5,
    '海报': 0
}
goods['唱片'] = {
    '架子鼓': 20,
    '吉他': 15,
    '海报': -7
}
goods['海报'] = {
    '吉他': 30,
    '架子鼓': 35
}
goods['吉他'] = {
    '钢琴': 20,
}
goods['架子鼓'] = {
    '钢琴': 10,
}
goods['钢琴'] = {
}

if __name__ == '__main__':
    res = OrderedDict()
    res['乐谱'] = 0
    que = queue.Queue()
    que.put('乐谱')
    while not que.empty():
        t = que.get()
        for i in goods[t]:
            que.put(i)
            new = res[t] + goods[t][i]
            if i not in res:
                res[i] = new
            elif new < res[i]:
                res[i] = new
    print(res)
