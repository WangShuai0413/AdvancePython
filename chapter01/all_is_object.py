# /bin/python3
# -*- coding:utf-8 -*-
"""
Python中一切皆为对象
"""

# 函数可以被赋值给变量
def hello(name='world'):
    print('hello ' + name)

# my_func = hello
# my_func('python')

# 类可以被赋值给变量
class Person:
    def __init__(self):
        print('__init__')

# my_class = Person
# my_class()

# 可以添加到集合对象中

# 定义集合对象
obj_list = []
# 添加方法与类到几个中
obj_list.append(hello)
obj_list.append(Person)

# for item in obj_list:
#     print(item())

## 可以作为参数传递给函数
def print_type(item):
    print(type(item))

# for item in obj_list:
#     print_type(item)


# 可以当做函数返回值
def decorator_func():
    print('调用decorator_func函数')
    return hello

my_func = decorator_func()
my_func('python')
