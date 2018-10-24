from collections import OrderedDict

info = OrderedDict()
info['水'] = {
    'w': 3,
    'v': 10
}
info['书'] = {
    'w': 1,
    'v': 3
}
info['食物'] = {
    'w': 2,
    'v': 9
}
info['夹克'] = {
    'w': 2,
    'v': 5
}
info['相机'] = {
    'w': 1,
    'v': 6
}

info2 = {
    '水': {
        'w': 3,
        'v': 10
    },
    '书': {
        'w': 1,
        'v': 3
    },
    '食物': {
        'w': 2,
        'v': 9
    },
    '夹克': {
        'w': 2,
        'v': 5
    },
    '相机': {
        'w': 1,
        'v': 6
    },

}


def func(goods, bag):
    before_value = [0 for i in range(bag)]
    for _, good in goods.items():
        result_value = []
        for b in range(1, bag + 1):
            left_w = b - good['w']
            if left_w >= 0:
                temp_value = good['v'] + (before_value[left_w - 1] if left_w > 0 else 0)
                old_vaule = before_value[b - 1]
                new_value = max(temp_value, old_vaule)
            else:
                new_value = before_value[b - 1]
            result_value.append(new_value)
        print(result_value)
        before_value = result_value


# 动态规划
if __name__ == '__main__':
    func(info2, 6)
