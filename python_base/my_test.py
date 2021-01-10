#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@author: hyb
@file: my_test.py
@time: 2021/01/10
"""

if __name__ == '__main__':
    # 列表推导式
    my_list1 = [i ** 2 for i in range(1, 20) if i > 10]
    # 循环嵌套
    my_list2 = [str(i) + j for i in range(1, 6) for j in "abcde"]
    # 用推导式将字典转换为列表
    my_dict = {
        'a': "张三",
        'b': "李四"
    }
    my_list3 = [key + ':' + value for key, value in my_dict.items()]
    # 推导式生成字典
    my_dict1 = {k: k ** 2 for k in range(1, 10)}
    # 推导式实现字典的k-v互换
    my_dict2 = {v: k for k, v in my_dict.items()}
    # 推导式生成集合
    my_set = {i for i in "sidfhjsiodfjsiodfhjso" if i not in "fh"}
    print("列表生成式例子：")
    print(f"列表推导式：{my_list1}")
    print(f"循环嵌套：{my_list2}")
    print(f"用推导式将字典转换为列表：{my_list3}")
    print(f"推导式生成字典：{my_dict1}")
    print(f"推导式实现字典的k-v互换：{my_dict2}")
    print(f"# 推导式生成集合：{my_set}")

    # 生成器
    my_generator = (i for i in range(1, 50))
    print(f"列表生成器：")
    print(my_generator)
    print(list(my_generator))

    # python 三元运算符
    print("python的三元运算符：")
    i = 10
    a = "True" if i >= 10 else "False"
    print(a)
