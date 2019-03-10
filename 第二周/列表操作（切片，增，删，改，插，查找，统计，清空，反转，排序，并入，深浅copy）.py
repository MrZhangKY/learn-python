#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/13 15:10'
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

#1,列表操作
# a = [1, 2, 3, 4]
# print(a)
# print(a[0], a[2])
# print(a[1:3])   #正着切片，顾头不顾尾
# print(a[0:4])
#
# print(a[-1])    #不知道列表有多长，取最后一个
# print(a[-3:-1]) #倒着切片，顾头不顾尾
# print(a[-3:])   #取之后所有值
# print(a[1:])
#
# print(a[0:-1:2])    #可以设定步长
# print(a[::2])   #(0,-1)可以省略
#
# #增
# a.append(5)
# print(a)
#
# #插
# a.insert(1, 1.5)  #想插在哪，写那个位置
# print(a)
#
# a.insert(3, 2.5)
# print(a)
#
# #改
# a[2] = 2.1
# print(a)
#
# #删
# #remove，写要删掉谁
# a.remove(2.1)
# print(a)
#
# #del，写下标，不写下标，连变量一起删除
# del a[1]
# print(a)
#
# #pop，不写下标默认最后一个，写下标与del相同
# a.pop()
# print(a)
#
# a.pop(1)
# print(a)
#
# #查找
# print(a.index(4))
#
# #统计
# a.append(4)
# print(a.count(4))
# print(a)
#
# # #清空
# # b = a
# # b.clear()
# # print(b)
#
# #反转
# a.reverse()
# print(a)
#
# #排序（特殊字符，数字，大写，小写，ascii规则）
# a.sort()
# print(a)
#
# #并入
# b = [6, 4, 5]
# a.extend(b)
# print(a,b)
#
# #复制(copy浅copy，只copy第一层)([]中套一个[],这个[]是一个指针，如果copy后改哪个[]中的值，都会改)
#
# a.append([6,'a'])
# print(a)
#
# c = a.copy()
#
# a[0] = 0
# a[7][0] = 1
# print(c)    #c里6改为1了
#
# c[7][1] = 'b'
# print(a)    #a里a改为b了
#
# #其实列表，元组，字典都是指一块内存，都不能通过等号防止后来的变化(=连浅层都没有)，与数字、字符串不同
# d = [1,2,3]
# e = d
# d[1] = 'a'
# print(e)
#
# #如果要完整的copy，需要引入copy模块的deepcopy方法，会形成完全独立的列表(占不同的内存)
# import copy
# e = copy.deepcopy(a)
# a[7][0]= 2
# print(e)
# print(a)

#2对浅copy的补充
#浅copy的意义是 对被copy列表元素的共同引用，其实现方法有4，作用主要用于多个列表有公用的部分，如下例

# person = ['name', ['saving', 1000000]]
# # p1 = copy.copy(person)
# # p2 = person.copy()
# # p3 = person[:]
# # p4 = list(person)
# #
# # print(p1, p2, p3, p4)
#
# #应用例，两人公用存款
# p1 = person[:]
# p2 = person[:]
#
# p1[0] = "张开宇"
# p2[0] = "@@"
#
# p1[1][1] = @@@@@@@@@@
#
# print(p1)
# print(p2)

#3,enumerate,返回下标
a = [1,2,3]
for index, _a in enumerate(a):
    print(index,_a)

for _a in a:
    print(a.index(_a), _a)

for i in enumerate(a):
    print(i)

#4，带色输出
print('\033[44;1m  好玩吧？  \033[0m')
print('\033[41;1m  我爱@@！  \033[0m')
