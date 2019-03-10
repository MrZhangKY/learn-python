# -*- coding:utf-8 -*-
# Author : 张开宇
# Data : 2018/11/4 20:46
#

#0，变量命名可为英文，数字，_，中文。数字不可打头，不可用特殊字符。

#1,'''的作用

#1.1,多行注释
'''print()
print()
print()'''

#1.2,格式化输出
a = '''
我叫张开宇
我今年**岁
我在****大学
我正在**
'''
print(a)

#1.3 '与"在输出的时候无区别，只有一种情况要注意：单套双，双套单
a="i'm zhang kai yu"
print(a, '\n')

# #2,用户输入
# username = input("uesrname:")
# password = input("password:")
# print(username, password)

#2.1,用户输入格式化输出
name = input("name:")

age = input("age:")
#print(type(age))#注意此处，输入就算是数字也是str型

job = input("job:")
salary = input("salary:")

# #2.1.1,字符串加减（太low了，忘记它吧）
# info = '''-----info of '''+name+'''-----
# age:'''+age+'''
# job:'''+job+'''
# salary:'''+salary
#
# print(info)

# #2.1.2，外部引入，棒棒的~,利用%s或者%d等传入
#
# info = '''
# -----info of %s-----
# name:%s
# age:%s
# job:%s
# salary:%s
# ''' % (name, name, age, job, salary)
#
# print(info)

# #注意：输入的是str型，如果age处改为%d，需要强转格式
#
# info ='''
# -----info of %s-----
# name:%s
# age:%d
# job:%s
# salary:%d
# ''' % (name, name, int(age), job, int(salary))
#
# print(info)

# #2.1.3外部引入，用{}引入，{}内可为任意值，建议变量名加_,另外{}内相同符号不用再赋值,建议用！！！！！！！！！！！！
# info = '''
# -----info of {_name}-----
# name:{_name}
# age:{lalalalalala}
# job:{_job}
# salary:{工资}
# '''.format(_name=name,
#            lalalalalala=age,
#            _job=job,
#            工资=salary)
# print(info)

#2.1.4{}按照顺序引入
info = '''
-----info of {0}-----
name:{0}
age:{1}
job:{2}
salary:{3}
'''.format(name, age, job, salary)

print(info)
