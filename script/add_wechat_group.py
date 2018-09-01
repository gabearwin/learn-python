# 脚本6
from wxpy import *
import time

# 建议使用小号建群，运行代码时用小号扫码登录，避免大号被封。
# 运行代码之前需要先建好群，修改群名称和代码中一致，至少在群里说一句话。
bot = Bot()

def get_newfren(say):
    """
    添加好友时，如果验证信息为say，则把消息加入列表

    :param say: 加好友时的验证信息
    :return: 所有加好友的消息集合
    """
    time.sleep(10)
    return [msg for msg in bot.messages if msg.text == say]

def listen(pwd):
    """
    当好友发送加群关键字pwd时，把此消息加入列表

    :param pwd: 加群关键字
    :return: 所有需要加群的消息集合
    """
    time.sleep(10)
    return [msg for msg in bot.messages if msg.text == pwd]

def add(users, group):
    try:
        group.add_members(users, use_invitation=True)
        return group
    except ResponseError:
        return None

group = bot.groups().search('test group')[0]

while True:
    new_friend = get_newfren('Make friend')
    if new_friend:
        print('Found a new friend!')
        for msg in new_friend:
            # 加好友的消息是msg，通过msg.card获取此好友，自动通过好友验证并发送一句问候语
            new_user = msg.card
            bot.accept_friend(new_user)
            new_user.send('Hi new friend')
            bot.messages.remove(msg)  # 注意此处需要在总的消息池中移除此消息
    time.sleep(10)
    print('Running')
    selected = listen('Pull me in')
    if selected:
        print('Found one want to join group!')
        for msg in selected:
            # 好友发送的消息是msg，通过msg.sender获取此好友，自动给他发送加群邀请
            this_user = msg.sender
            add(this_user, group)
            bot.messages.remove(msg)
