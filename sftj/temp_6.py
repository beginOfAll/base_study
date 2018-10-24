stations = {
    'kthree': {'nv', 'ca', 'or'},
    'kfour': {'nv', 'ut'},
    'ktwo': {'mt', 'wa', 'id'},
    'kone': {'nv', 'ut', 'id'},
    'kfive': {'az', 'ca'}
}

states_needed = {"mt", "wa", "or", "id", "nv", "ut",
                 "ca", "az"}


def temp():
    remain_stations = dict(stations)
    remain_states = set(states_needed)
    result = list()
    while len(remain_states) > 0:
        targe = None
        score = 0
        for one in stations:
            temp = len(stations[one].intersection(remain_states))
            if temp > score:
                targe = one
                score = temp
        if score > 0:
            result.append(targe)
            remain_states.difference_update(remain_stations.pop(targe))
        else:
            break
    print('结果', result)
    print('剩余', remain_states)


# 贪婪算法, 局部最优解
if __name__ == '__main__':
    temp()
