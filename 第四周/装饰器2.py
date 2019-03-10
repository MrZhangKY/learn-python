#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/25 14:05'
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
'''被装饰函数无返回参数，有返回参数，装饰器本身有参数判断该'''

user, passwd = '张开宇', '！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！'

'''1，被装饰的函数有返回值'''
# def auth(func):
#     def wrapper(*args, **kwargs):
#         username = input('username:').strip()
#         password = input('password:').strip()
#
#         if user==username and passwd==password:
#             print('\033[32;1muser has passed\033[0m')
#             res = func(*args, **kwargs)
#             return res #函数的返回值
#         else:
#             print('\033[31;1mwrong\033[0m')
#     return wrapper
#
# def index():
#     print('welcome to index page')
#
# @auth
# def home():
#     print('welcome to home page')
#     return 'home page'
#
# index()
# # home()
# print(home())

'''2，装饰器添加一层判断，根据判断执行不同函数'''
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):

            if auth_type=='local':
                username = input('username:').strip()
                password = input('password:').strip()

                if user==username and passwd==password:
                    print('\033[32;1muser has passed\033[0m')
                    res = func(*args, **kwargs)
                    return res #函数的返回值
                else:
                    print('\033[31;1mwrong\033[0m')
            else:
                pass

        return wrapper
    return out_wrapper

def index():
    print('welcome to index page')

@auth(auth_type = 'local')
def home():
    print('welcome to home page')
    return 'home page'

@auth(auth_type = 'abc')
def bbs():
    print('welcome to bbs page')
    return 'bbs page'

index()
# home()
print(home())
bbs()
