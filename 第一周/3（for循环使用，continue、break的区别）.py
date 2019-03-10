#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '张开宇'
__mtime__ = '2018/11/5 10:40'
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
# #1，for循环
# for i in range(10):
#     print("loop: ",i)

# #1.1,for与if的结合
# age_of_zhangkaiyu = ￥￥
# for i in range(3):
#     age_guess = int(input("guess age:"))
#     if age_guess == age_of_zhangkaiyu:
#         print("yes, you got it!")
#         break
#     elif age_guess>age_of_zhangkaiyu:
#         print("guess less!")
#     else:
#         print("guess bigger!")
# else:
#     print("fuck off, your have tried too many times!")

# #1.3,for 等间隔输出
# for i in range(0, 10, 2):
#     print("loop: ", i)

# #1.4, 游戏进一步完善,私服版本
# age_of_zhangkaiyu = ￥￥
# i = 0
# while i<3:
#     guess_age = int(input("guess age:"))
#     if guess_age == age_of_zhangkaiyu:
#         print("congratulations, you have got it!")
#         break
#     elif guess_age>age_of_zhangkaiyu:
#         print("guess less!")
#     else:
#         print("guess more!")
#     i+=1
#     if i == 3:
#         continue_confirm = input("do you want to guess again?")
#         if continue_confirm != 'n' and continue_confirm !='N':
#             i=0
#         else:
#             print("fuck off, you have tried too many times!")

# #2,CONTINUE的含义:break是打断，结束当前整个循环；continue是跳出本次循环，进行下一个循环
# for i in range(10):
#     if i<3:
#         print("loop: ", i)
#     else:
#         continue
#     print("he he")

#2.1,对比,循环嵌套
for i in range(10):
    print('----------',i)
    for j in range(10):
        print(j)
        if j>5:
            break
