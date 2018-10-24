def sub_string(s1, s2):
    mm = [[0 for i in range(len(s2))] for j in range(len(s1))]
    max_len = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                before = mm[i - 1][j - 1] if (i > 0 and j > 0) else 0
                mm[i][j] = before + 1
                if mm[i][j] > max_len:
                    max_len = mm[i][j]
                    p = j
    return s2[p - max_len + 1:p + 1]


def sub_serial(s1, s2):
    mm = [[0 for i in range(len(s2))] for j in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                before = mm[i - 1][j - 1] if (i > 0 and j > 0) else 0
                mm[i][j] = before + 1
            else:
                mm[i][j] = max(mm[i - 1][j], mm[i][j - 1])
    return mm


# 最长公共子串 属动态规划
# 最长公共子序列
if __name__ == '__main__':
    m = sub_string('blue', 'clues')
    print(m)
