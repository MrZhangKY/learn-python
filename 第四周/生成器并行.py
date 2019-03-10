#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/26 13:05'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import time

def consumer(name):
    print('{name} 准备吃包子了'.format(name=name))
    while True:
        baozi = yield
        print('包子{number}来了，被{name}吃了'.format(number=baozi, name=name))

def procedure(name):
    c = consumer('a')
    c1 = consumer('b')
    c.__next__()
    c1.__next__()
    print('准备做包子了')
    for i in range(10):
        time.sleep(1)
        print('{name}做了个包子，一人一半'.format(name=name))
        '''send 的值传给yield，next不传'''
        c.send(i)
        c1.send(i)

procedure('d')
