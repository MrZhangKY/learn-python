#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/25 14:40'
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
'''1,列表生成式'''
# print([i*2 for i in range(10)])
#print([func(i) for i in range(10)])

'''2，生成器，边循环边生成，用到的时候生成相应的数据，可以节省内存空间
但缺点是不支持切片、和索引取值这些操作，只能通过for循环一个个取元素
'''

'''生成器：中括号变小括号'''
# b = (i*2 for i in range(10))
# print(b)
# # for i in b:
# #     print(i)
#
# '''有一个方法.__next__()，可以一个个向下，但不可退回
# 本质是生成器只记录当前位置'''
# b.__next__()
# b.__next__()
# print(b.__next__())

'''3，用函数生成生成器，用yield'''
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n<max:
#         #print(b)
#         yield b
#         a, b = b, a+b
#         '''这句话相当于
#         t = (b, a+b)
#         a = t[0]
#         b = t[1]
#         '''
#         n+=1
#     return('----done----')
#
# # f = fib(100)
# # '''中断，可以出来干点事'''
# # print(f.__next__())
# # print('haha')
# # print(f.__next__())
# # print('出来了')
# # print(f.__next__())
# # print('进去了')
# # print(f.__next__())
# # print('又出来了')
# # print(f.__next__())
# # print('又进去了，多线程的感觉？')
# # print(f.__next__())
# #
# # print('start loop')
# # for i in f:
# #     print(i)
#
# '''一直next超出范围会报错，可以抓住那个异常'''
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('generator return value:', e.value)
#         break

'''4,
可以直接用于for循环的数据类型有以下几种：
一类是集合数据类型：str,set,list,dic,tuple
一类是generator,包括生成器和带有yield的generator function
这些可以直接作用于for循环的对象统称为可迭代对象：iterable
可以使用isinstance()判断一个对象是否为iterable
'''
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance(100, Iterable))

'''可以被next函数调用并不断返回下一个值的对象成为迭代器:Iterator
range就是一个迭代器'''

