#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/19 14:01'
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
#1,直接操作
# data = open('yesterday.txt').read()
# print(data)

# data = open('yesterday', encoding='utf-8').read()
# print(data)

#2,文件句柄（文件名，字符集，大小，硬盘起始位置），写
# f = open('yesterday', 'r', encoding='utf-8')
# data1 = f.read()
# data2 = f.read()
# print(len(data1))
# print(len(data2))   #文件指针在一次内存操作中，不会自己重新回去

# #3，打开文件模式，写，内容就被冲掉了
# f = open('yesterday2', 'w', encoding='utf-8')
# f.write('lalala,\nlalala')

# #4，追加模式，可在文件最后添加内容,不可读
# f = open('yesterday2', 'a', encoding='utf-8')
# f.write('\nlalala')

#5，按行读取

# low loop readlines 只适合小文件的写法，内存可能会爆掉
'''
f = open('yesterday', 'r', encoding='utf-8')
# print(f.readline())
#
# for i in range(5):
#     print(f.readline())

# print(f.readlines())

# for line in f.readlines():
#     # print(line)
#     print(line.strip()) #去除空格和换行

for index, line in enumerate(f.readlines()):
    if index==9:
        print('-------------------------')
        continue
    print(line.strip())
'''

#6，针对大文件, readline好像效果也可以
f = open('yesterday', 'r', encoding='utf-8')

for i in range(10):
    data = f.readline()
    print(data.split())
    print(data)

for line in f:
    print(len(line))
    print(line.strip())

#7，回头读取,tell打印当前位置，seek回到每个位置
#f = open('yesterday2', 'a', encoding='utf-8')
# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
# print(f.tell())
#
# #其他方法
# print(f.encoding)   #返回编码
# print(f.fileno())   #返回操作系统接口
# print(f.seekable()) #判断能否移光标
# print(f.readable())
# print(f.writable())
#f.truncate(20)  #文件打开形式为a

# f = open('yesterday2', 'w', encoding='utf-8')
# f.write('1')
# f.flush()   #将内存中的内容保证刷到硬盘中储存（保证实时存储，跟在write后面）

# 读写与写读
# f = open('yesterday2', 'r+', encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.write('lalalalalalalalla')    #没有更改，写在了最后一行，不覆盖文件
#
# f = open('yesterday2', 'w+', encoding='utf-8')  #用处不大。。。会覆盖
# f.write(';')


#8，文件修改，修改后的文件保存为一个新的文件
# f = open('yesterday', 'r', encoding='utf-8')
# f_new = open('yesterday2', 'w', encoding='utf-8')
#
# for line in f:
#     if "肆意的快乐" in line:
#         line = line.replace('等我', '等@@@O(∩_∩)O')
#     f_new.write(line)
#
# f.close()
# f_new.close()

# #9，with使用
# with open('yesterday', 'r', encoding='utf-8') as f: #超出with的执行范围，直接关闭（关闭的作用是释放内存）
#     for line in f:
#         print(line)
#
# #打开多个文件可以用
# with open('yesterday', 'r', encoding='utf-8') as f1, \
#       open('yesterday2', 'r', encoding='utf-8') as f2:
#     for line in f1:
#         print(line)
#     for line in f2:
#         print(line)
#
# #二进制rb,wb网络传输
# import struct
# f = open('data201801.dat', 'rb')
# Bytes = f.readlines()
# # print(struct.unpack('i',Bytes))
# for i in Bytes:
#     print(i)

# f = open('yesterday2', 'wb')
# f.write('lalala'.encode())  #看到的是utf-8




#练习
# with open('yesterday', 'r', encoding='utf-8') as f1, \
#       open('yesterday2', 'w', encoding='utf-8') as f2:
#     for line in f1:
#         if '蜡烛' in line:
#             line = line.replace('蜡烛', '@@')
#         #line = line.encode()
#         f2.write(line)

# with open('yesterday.txt', 'r') as f1, \
#       open('yesterday2.txt', 'w') as f2:
#     for line in f1:
#         print(line)
#         line_gbk = line.encode('gbk')
#         print(line_gbk)
#         f2.write(line_gbk.decode('gbk'))
#         print(line_gbk.decode('gbk'))
