#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: bingli
# Date: 2018.12.23
# Description: 文字游戏
# version: 0.0.1


from sys import argv, exit

# 解包
script_name, uname = argv

prompt = "> "

def start_print():
    """ 开头白，介绍游戏背景 """
    print "这天，你坐上了回家的大巴，你的家就在那神农架里的某个小镇里。"
    print "大巴马上就要启动了，请系好安全带，管理好自己的行李。"
    print "你四处看了看大巴发现大巴上人并不多，你猜他们可能是跟你一样是回家的人，不过不用多想就知道大部分人肯定是去神农架那边游玩。"
    print "大巴启动了。窗外的风景都被甩在了背后，你看着窗外觉得你有点困了"

def choose_awake(next):
    """ 选择睡觉，或者清醒 """
    flag = True

    while flag:

        if next == "休息" or next == "1":
            dead("在你睡觉的时候，发生了车祸，而你睡的跟猪一样，大巴发生了爆炸，你死于爆炸。")
        elif next == "不休息" or next == "2":
            flag = False
            level2()
        else:
            idk()
            next = raw_input(prompt)

def level2():
    """ 关卡2 """
    print "你处于清醒的状态，发生了车祸的同时成功逃生，逃脱了死亡威胁。"
    print "1. 与人们继续留在大巴附近。(留下来)"
    print "2. 独自一人去四周看看，四周非常的危险。（去冒险）"
    flag = True

    while flag:
        next = raw_input(prompt)

        if next == "留下来" or next == "1":
            dead("你选择留在这里，待在大巴附近，但是大巴爆炸了，突然一块玻璃飞过来，把你插死了。")
        elif next == "去冒险" or next == "2":
            flag = False
            print "你选择了探险，你沿着公路走，发现公路上有根电线，沿着这根电线走。"
            print "你不敢相信你自己的眼睛，居然看到一个剧组，上面还有大巴上的监控视频。好像是监控着一举一动。"
            print "你不敢相信这一切。"

            level3()
        else:
            idk()

def level3():
    """ 关卡3 """
    print "1. 冲上去跟他们干。（冲上去）"
    print "2. 逃跑到丛林去。（逃跑）"
    flag = True

    while flag:
        next = raw_input(prompt)

        if next == "冲上去" or next == "1":
            flag = False
            print "你通过了测试，你活了下来。干的漂亮！"
            exit(0)
        elif next == "逃跑" or next == "2":
            dead("你被发现了，被搜捕的人用枪给打死了。")
        else:
            idk()


def idk():
    """ 提示玩家输错命令了 """
    print "我看不懂你在说什么。"

def dead(reson):
    """ 输出死亡信息，并退出游戏 """
    print reson, "干的漂亮！"
    exit(0)

def start():
    """ 开始游戏 """
    print "--------------游戏开始--------------"
    start_print()

    print "1. 闭上眼睛，休息一会儿。(休息)"
    print "2. 不休息，看会小说（不休息）"

    next = raw_input(prompt)
    choose_awake(next)

start()
