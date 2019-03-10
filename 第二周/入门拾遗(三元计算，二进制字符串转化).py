#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/13 8:41'
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

# #1，三元运算
# a = 1
# b = 2
# c = 3
# result = a if b>c else b
# print(result)

#2,字符串与二进制的互相转换（网络编程传数据必须转）
msg = '我爱北京'
print(msg.encode())
print(msg.encode().decode())
print(type(msg.encode()))
print(type(msg.encode().decode()))
