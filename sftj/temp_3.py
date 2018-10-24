import queue
from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def is_mongo(name):
    if name[-1] == 'm':
        return True
    else:
        return False


# 广度优先搜索
if __name__ == '__main__':
    q = queue.Queue()
    searched = []
    for i in graph['you']:
        q.put(i)
    while not q.empty():
        t = q.get()
        if t not in searched:
            if is_mongo(t):
                print(t)
                break
            else:
                searched.append(t)
                for i in graph[t]:
                    q.put(i)
