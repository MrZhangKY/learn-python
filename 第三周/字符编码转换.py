#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/25 8:56'
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

import sys
print(sys.getdefaultencoding())

s = '啦'
print(s.encode('gbk'))
print(s.encode())

s_gbk = s.encode('gbk')
gbk_to_utf8 = s_gbk.decode('gbk').encode('utf8')    #decode是以哪种编码格式映射到unicode，encode是从unicode以哪种格式再出来

s_gb2312 = s.encode('gb2312')
print(s_gb2312)
print(type(s_gb2312.decode('gb2312')))
