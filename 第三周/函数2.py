#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/2 22:07'
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
#1，形参，实参，位置参数调用，关键字调用
def test(x, y):
    print(x)
    print(y)

'''位置参数调用'''
test(1,2)

'''关键字调用'''
test(y=2, x=1)

'''关键字参数是不能写在位置参数前面的！！'''
test(2, y=1)
#test(x=1, 2)

#2,默认参数
def test2 (x, y=2):
    print(x)
    print(y)

test2(3)
test2(3, 4)

'''调用函数的时候，默认参数非必须传递
用途：默认安装值，默认函数功能调用等'''

#3，参数组，针对传入的参数为多个，且个数不固定
def test3(*args):
    '''规范是args，此时为元组，只能接受”位置参数“，转化为元组'''
    print(args)

test3(1,2,5,6)
test3(*[[1, 2, 3, 4], [2, 4, 5]])
''' *形参，输入的多个参数按照元组处理'''

'''**kwargs为字典，这是另一种形式,将个数不固定的“关键字参数“转化为字典'''
def test4(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['wife'])

test4(name='@@@', age=@@, wife='@@')
test4(**{'name':'@@@', 'age':@@, 'wife':'@@'})

#4，局部变量与全局变量
def test5(name):
    '''局部变量，只在函数里生效'''
    print('before change', name)
    name = '@@'
    print('after change', name)

'''相应的，在程序的顶层定义的是全局变量'''
name = '@@@'
test5(name)
print(name)

'''当全局变量与局部变量重名时，在定义局部变量的子程序中，局部标量起作用，在其他地方，全局变量起作用'''

'''当然，在下层子结构中也可以用global声明全局变量'''
'''慎用慎用！'''
def test6(name):
    '''声明全局变量'''
    global name1
    print('before change', name1)
    name1 = '@@'
    print('after change', name1)
name1 = '张开宇'
test6(name1)
print(name1)

'''还要注意列表、字典、集合、类因为本身类似指针形式，利用局部变量可以修改全局的值（元组本身不可改）'''
'''字符串、数字不可改'''
def test7(name):
    name[0] = '张开宇'
    print('inside', name)

name = ['zhangkaiyu', '@@', '张且歌']
test7(name)
print('outside', name)
