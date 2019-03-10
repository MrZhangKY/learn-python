#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/19 11:20'
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

#1，去重
list_1 = [1, 1, 1, 2, 3, 4, 5, 5, 6]
list_1 = set(list_1)
print(list_1, type(list_1))

#2,关系测试
list_2 = set([3, 6, 7, 8, 9])

print(list_1.intersection(list_2))  #交集
print(list_1 & list_2)

print(list_1.union(list_2)) #并集，去重
print(list_1 | list_2)

print(list_1.difference(list_2))    #差集,1里去除2里有的
print(list_1 - list_2)

print(list_1.issubset(list_2))  #子集1是不是2的子集

print(list_1.issuperset(list_2))    #父集1是不是2的父集

print(list_1.symmetric_difference(list_2))  #对称差集，两个求并之后去除交
print(list_1 ^ list_2)

print(list_1.isdisjoint(list_2))    #无交集返回真

#增删改查
list_1.add(999)
print(list_1)

list_1.update([111,222,233])
print(list_1)

