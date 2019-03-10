#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/8 13:32'
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

'''
装饰器本质是函数，

功能：是用来装饰其他函数，就是为其他函数添加附加功能

原则：
1，不能修改被装饰函数的源代码
2，不能修改被装饰函数的调用方式
3，增添新功能
总之：装饰器对被修饰的函数是完全透明的
     
实现装饰器知识储备：
1，函数即‘变量’，定义函数就是将函数体赋值给函数名，与变量的内存回收机制一样
2，高阶函数
    a：把一个函数名当作实参传给另一个函数
    b：返回值中包含函数名
3，嵌套函数
4，高阶函数+嵌套函数-》装饰器
'''

#1，函数也有内存地址
# def pass1():
#     print('pass')
#
# print(pass1)
#
# pass1()
#
# print(pass1())
# '''默认返回值NONE'''

#2，高阶函数
import time

def bar():
    time.sleep(3)
    print('in the bar')

# fun = bar
# fun()

def first(func):
    '''一个函数，附加了功能，没有改变源代码，但是调用方式变了
    输入中有函数名，可以做到在不修改源代码的情况下，增添功能'''
    start_time = time.time()
    func()
    end_time = time.time()
    print('{function} running time: {time}'.format(function=func, time=end_time-start_time))
#first(bar)  #函数名就是变量名就是内存地址，（）表示调用函数体

def second(func):
    '''一个函数，附加了功能，没有改变源码，调用方式未变
    返回中有函数名，可以做到在不修改调用方式的情况下，增添功能'''
    print(func)
    return func
#print(second(bar))
#second(bar())
#second(bar)()
'''牛逼的来了，未修改调用方式，增添了功能'''
# bar = second(bar)
# bar()

#3，嵌套函数
def foo():
    print('in the foo')
    def bar():
        '''嵌套函数，只能内部调用，是在一个函数体内，用def去声明一个函数（可不是调用）'''
        print('in the bar')
#     bar()
# foo()

#4，装饰器
def deco(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print('{func} runing time : {time}'.format(func=func, time=end_time-start_time))

def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)  #first()
        end_time = time.time()
        print('{func} runing time : {time}'.format(func=func, time=end_time-start_time))
    return deco

@timer #first = timer(first)=deco  first()=deco()
def first():
    time.sleep(3)
    print('in the first')

@timer
def second(name):
    time.sleep(3)
    print('in the second:', name)

# first()
# second('张开宇')

#5，装饰器高级版
def index():
    print('welcome to index page')

def home():
    print('welcome to home page')

def bbs():
    print('welcome to bbs page')

# user, password = '张开宇', '！！！！！！！！！！！！！！！！'
# def log_in(func):
#     def deco(*args, **kwargs):

