#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/26 8:09'
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

# # 1，面向过程与函数式编程
#
#
# def func1():
#     """testing1"""
#     print('in the func1')
#     return 0    # 函数式编程有return
#
#
# def func2():
#     """testing2"""
#     print('in the func2')   # 面向过程无返回值
#
#
# x = func1()
# y = func2()
#
# print('in the func1 return is %s' %x)
# print('in the func2 return is %s' %y)

# # 2,使用函数的好处,代码重用，保持一致性，可扩展性好
# # 以写文件日志为例
# import time
#
#
# def log():
#     """追加文件日志操作记录及时间"""
#     time_format = '%Y-%m-%d %X'
#     time_current = time.strftime(time_format)
#     with open('日志_文件操作.txt', 'a') as f:
#         f.write('%s 进行一次修改或操作\n' %time_current)
#
#
# def test1():
#     """test1"""
#     print('test1')
#     log()
#
#
# def test2():
#     """test2"""
#     print('test2')
#     log()
#
#
# def test3():
#     """test3"""
#     print('test3')
#     log()
#
#
# test1()
# test2()
# test3()

#3，函数可以返回的值
def test1():
    """test"""
    print('test1')

def test2():
    """test"""
    print('test2')
    return 0

def test3():
    """test"""
    print('test3')
    return 1, '@@@', ['@@@', '@@'], {'@@':'@@@', '@@':'@@'} #return个数类型均不固定

# print(test1())
# print(test2())
# print(test3())
a = test3()
print(a)
