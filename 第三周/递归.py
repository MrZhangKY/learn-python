#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/3 16:11'
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
#1,递归是自己调自己，但是递归有最大深度999，先来个死循环
# def death(n):
#     '''递归——返回函数名'''
#     print(n)
#     return death(n+1)
# death(0)
'''RecursionError: maximum recursion depth exceeded while calling a Python object'''

'''
递归特性：
1，必须有一个明确的结束条件
2，每次进入深一层递归时，问题规模相对于上一层都应有所减少
3，递归效率不高，递归层数过多时会造成栈溢出
'''


'''注意以下两段代码的区别'''
# def clac(n):
#     print(n)
#     if n/2>0:
#         return clac(n/2)
# clac(10)

def clac(n):
    print(n)
    if int(n/2)>0:
        return clac(int(n/2))
    print('->', n)
clac(10)

'''函数式编程的一个特点是：允许把函数本身作为一个参数传入另一个函数、并且返回值也可以是一个函数
函数是编程的语言有：lisp、hashshell、erlang，python仅支持部分函数式编程（tensorflow好像是一种。。）
函数式编程是一种编程范式'''

'''
2,高阶函数
变量可以指向函数、函数的参数能够接收变量，
那么一个函数就可以接受另外一个函数作为参数，
这种函数被称为高阶函数
'''
def add(x,y,f):
    return f(x)+f(y)

res = add(3, -6, abs)
print(res)
