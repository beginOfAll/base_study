from collections import OrderedDict
import queue

group2 = {
    'BEGIN': {'A': 5, 'B': 2},
    'A': {'C': 4, 'D': 2},
    'B': {'A': 8, 'D': 7},
    'C': {'D': 6, 'END': 1},
    'D': {'END': 1},
    'END': {},
}

group3 = {
    'BEGIN': {'A': 10},
    'A': {'B': 20},
    'B': {'C': 1, 'END': 30},
    'C': {'A': 1},
    'END': {},
}
group4 = {
    'BEGIN': {'A': 2, 'B': 2},
    'A': {'C': 2, 'END': 2},
    'B': {'A': 2, },
    'C': {'B': -1, 'END': 2},
    'END': {},
}


def dijkstra(group, begin='BEGIN', end='END'):
    cost = OrderedDict()
    cost[begin] = 0
    parents = OrderedDict()
    processed = []
    que = queue.Queue()
    que.put(begin)
    while not que.empty():
        node = que.get()
        if node not in processed:
            for next_node in group[node]:
                que.put(next_node)
                new = cost[node] + group[node][next_node]
                if next_node not in cost or new < cost[next_node]:
                    cost[next_node] = new
                    parents[next_node] = node
            processed.append(node)
    print(cost)
    print(parents)
    print(processed)


def breadth_first(group, begin='BEGIN', end="END"):
    q = queue.Queue()
    parents = OrderedDict()
    processed = []
    q.put(begin)
    while not q.empty():
        t = q.get()
        if t not in processed:
            if t == end:
                print(t)
            else:
                for i in group[t]:
                    q.put(i)
                    if i not in parents:
                        parents[i] = t
            processed.append(t)
    print(parents)
    print(processed)


# 加权有向图 狄克斯特拉算法
if __name__ == '__main__':
    dijkstra(group4)
