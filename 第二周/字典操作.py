#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/11/17 11:25'
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

#1，创建字典 key-value
info = {
    '@@': '张开宇',
    '@@': '@@'
}
print(info)
print(info['@@'])

info['@@'] = '@@@@'
print(info)

del info['@@']
print(info)

info['@@'] = '@@@'
print(info)

info.pop('@@')
print(info)

print(info.get('@@'))   #安全获取
print(info.get('@@'))

print('@@' in info and '@@' in info)
print('@@' in info)

print(info.values())
print(info.keys())

info.setdefault('@@', '???')    #有则不动，无则添加
info.setdefault('@@', '???')
print(info)

#update,两字典重叠覆盖，无则添加
info1 = {
    '@@': '@@',
    '@@': '@@@'
}
info.update(info1)
print(info)

print(info.items())

#循环
for i in info:
    print(i, info[i])   #高效

for k, v in info.items():
    print(k, v) #效率较低

# #初始化新字典
# c = dict.fromkeys([6,7,8], ['test', ['lala']])
# print(c)
# c[6] = 'ha'
# print(c)
# c[7][1] = 'cao'
# print(c)

# #2,嵌套(手动滑稽)
# av_catalog = {
#     '欧美': {
#         'www.youporn.com': ['很多免费的，世界最大的', '质量一般'],
#         'www.pornhub.com': ['很多免费的，也很大', '质量比youborn高点'],
#         'letmedothistoyou.com': ['多是自拍，高质量图片很多', '资源不多，更新慢'],
#         'x-art.com': ['质量很高，真的很高', '全部收费']
#     },
#     '日韩': {
#         'tokyo-hot': ['质量怎样不清楚', '听说收费']
#     },
#     '大陆': {
#         '1024': ['全部免费，真好，好人一生平安', '服务器在国外，慢']
#     }
# }
#
# print(av_catalog)
