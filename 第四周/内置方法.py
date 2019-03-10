#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/30 12:30'
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
#1,all，判断可迭代对象，所有为真返回真
# print(all([-1])) #非零即真
# print(all([0]))

#2,any，判断可迭代对象，有真返回真
# print(any([0, 1, 2]))
# print(any([0, 0]))

#3,ascii???中文返回二进制编码？
# print(ascii([1, '拉拉']))
#
# a = ascii(['拉拉'])
# b = ['拉拉']
# if a==b:
#     print('duide')    #二进制与中文字符好像并不相同
#
# print(type(a))  #字符串，变量类型转换了
# print(type(b))  #列表
# print([a])

#4,bin,十进制转二进制
#print(bin(255))

#5,bool判断真假
# print(bool(0))
# print(bool(1))
# print(bool([]))
# print(bool([0]))

#6,bytearray,可修改的二进制字符串格式
# '''字符串不能通过调用下标修改，下标只能用于调用'''
# a = 'aaaaa'
# # for i in a:
# #     a[i] = 'b'
# print(a)
# a = 'bbbbb'
# print(a)
#
# a = bytes('aaaaa', encoding='utf-8')
# print(a.capitalize(), a)
# #a[0] = 'b'
#
# a = bytearray('aaaaa', encoding='utf-8')
# # for i in a:
# #     print(i)
# for i in range(len(a)):
#     a[i] = 98
# print(a)

#7,callable,判断是否可调用,可以加（）的是可调用，目前知道的也只有函数和类
def lala():
    pass

print(callable(lala))
print(callable([]))
