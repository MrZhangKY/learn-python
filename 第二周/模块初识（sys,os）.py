#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/12 11:11'
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

#1,sys
import sys
print(sys.path)
print(sys.path[1])
print(sys.argv)
print(sys.argv[0])

#2,os（os的作用是与系统交互）

# #2.1
# import os
# cmd_res = os.system('dir')#直接调用系统命令,执行命令，不保存结果
# print("-->", cmd_res)

# #2.2
# import os
# cmd_res = os.popen('dir').read()#返回值位内存地址，.read读取内存中的内容
# print("-->", cmd_res)
# os.mkdir('new_dir')#创建目录，目录==文件夹

#2.3 import 找文件先找当前目录，没有去找全局变量，如果调用的文件不再当前目录下，有两种操作方法
#一是将脚本拷到‘环境变量’（即当前可以调入的路径）下，二是改变环境变量
