from wxpy import *
import time
import random

snt_list = list()
with open('/home/wjz/PycharmProjects/base_wjz/wechat/snt.txt', 'rt') as f:
    for line in f:
        line = line.strip()
        snt_list.append(line)
snt_list = snt_list[:10000]


def open_bot():
    bot = Bot()
    wxpy_group = bot.groups().search('金橙污大帅逼')[0]

    for i in range(100):
        time.sleep(10)
        wxpy_group.send('陈佳健' + random.choice(snt_list))

    bot.join()


if __name__ == '__main__':
    open_bot()
