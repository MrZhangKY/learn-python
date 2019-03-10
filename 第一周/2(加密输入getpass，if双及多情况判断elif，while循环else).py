#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '张开宇'
__mtime__ = '2018/11/4 23:37'
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

# #1，加密输入（输入不显示）getpass,(pycahrm不支持getpass模块)
# import getpass
# username = input("username:")
# password = getpass.getpass("password:")
# print(username, password)

#2,if条件判断

# #2.1,两种情况if，else
# _username="zhangkaiyu"
# _password="￥￥￥￥￥￥￥￥￥￥￥"
#
# username=input("username:")
# password=input("password:")
#
# if _username==username and _password==password:
#     print("welcome user {name} login!".format(name=username))
# else:
#     print("invalid username or password!")

# #2.2,三种及其以上种情况，可以嵌套，可以用elif
# age_of_zhangkaiyu = ￥￥
# guess_age = int(input("guess age:"))
#
# # if guess_age == age_of_zhangkaiyu:
# #     print("you have got it!")
# # else:
# #     if guess_age > age_of_zhangkaiyu:
# #         print("please guess less")
# #     else:
# #         print("please guess bigger")
#
# if guess_age == age_of_zhangkaiyu:
#     print("you have got it!")
# elif guess_age > age_of_zhangkaiyu:
#     print("please guess less")
# else:
#     print("please guess bigger")

#3，while循环

# #3.1 无限循环
# count = 0
# while True:
#     print("count:",count)
#     count +=1    #等价于 count = count + 1

# #3.2 有限循环
# count = 0
# while True:
#     print("count:", count)
#     count +=1
#     if count == 1000:
#         break

#4,if与while联合使用,while 可与else联用，意思是在while循环内没有break，而是通过while的条件break，则执行else内的内容。

# #4.1
# _username = 'zhangkaiyu'
# _password = '￥￥￥￥￥￥￥￥￥￥￥'
# num = 0
#
# while num<3:
#     username = input("username:")
#     password = input('password:')
#     if _username == username and _password==password:
#         print("welcome user {name} login!".format(name=username))
#         break
#     else:
#         print("invalid username or password")
#     num +=1
# else:
#     print("you have trid too many times, fuck off!")

#4.2
age_of_zhangkaiyu = ￥￥
num = 0

while num<3:
    guess_age = int(input("guess_age:"))
    if guess_age == age_of_zhangkaiyu:
        print("you have got it!")
        break
    elif guess_age > age_of_zhangkaiyu:
        print("guess less")
    else:
        print("guess bigger")
    num+=1
else:
    print("you have tried too many times, fuck off!")
