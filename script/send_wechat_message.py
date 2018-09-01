# 脚本 4/5
import csv
from wxpy import *
import time

def read_info():
    f = open('./wechat.csv', 'r', encoding='UTF-8')  # 读取中文需要设置字符编码
    reader = csv.DictReader(f)  # 读取之后作为字典存储
    return [info for info in reader]  # [{},{},{}] #将很多字典装成一个list

def send(info_list):
    bot = Bot()
    for info in info_list:
        friend_name = info['name']
        f = bot.friends().search(friend_name)  # list
        if len(f) == 1:
            try:
                f[0].send(make_msg(info))
            except ResponseError as e:
                print("stop at" + friend_name + e.err_code + e.err_msg)
        else:
            print(friend_name)
            print('Please check this name')
    time.sleep(3)  # 防止发送消息过快

def make_msg(info):
    t = "Hi {n}，我想对你说{m}。"
    return t.format(n=info['name'], m=info['message'])

info_list = read_info()
send(info_list)
