"""
Author: Zirui Wang
Date: 2021-09-21 18:13:25
LastEditTime: 2021-09-22 08:55:27
LastEditors: Please set LastEditors
Description: First lab
FilePath: \AlgorithmCode\lab1.py
"""
from matplotlib import pyplot as plt
from random import randint
from time import time
from copy import copy
def insert_sort(initial_list):
    """
    插入排序

    Args:
        initial_list (list): 初始数据列表

    Returns:
        list: 结果数据列表
    """
    length = len(initial_list)
    if length <= 1:
        return initial_list
    for i in range(length):
        target = initial_list[i]
        for j in range(i, -1, -1):
            if j == 0:
                initial_list[j] = target
                break
            if target < initial_list[j - 1]:
                initial_list[j] = initial_list[j - 1]
            else:
                initial_list[j] = target
                break
    result_list = initial_list
    return result_list


def merge_sort(initial_list):
    """
    归并排序

    Args:
        initial_list (list): 初始数据列表

    Returns:
        list: 结果数据列表
    """
    def merge(s1,s2,s):
        """将两个列表是s1，s2按顺序融合为一个列表s,s为原列表"""
        # j和i就相当于两个指向的位置，i指s1，j指s2
        i = j = 0
        length = len(s)
        while i+j<length:
            # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
            if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
                s[i+j] = s1[i]
                i += 1
            else:
                s[i+j] = s2[j]
                j += 1
    n = len(initial_list)
    # 剩一个或没有直接返回，不用排序
    if n < 2:
        return
    # 拆分
    mid = n // 2
    s1 = initial_list[0:mid]
    s2 = initial_list[mid:n]
    # 子序列递归调用排序
    merge_sort(s1)
    merge_sort(s2)
    # 合并
    merge(s1,s2,initial_list)
    return initial_list


def run():
    n_list = [10000,20000,30000,40000,50000]
    initial_list = [[[randint(0,n_list[k]) for i in range(n_list[k])] for j in range(10)] for k in range(len(n_list))]
    print(initial_list)
    insert_sort_list =copy(initial_list)
    merge_sort_list = copy(initial_list)
    begin = time()
    insert_sort_list_result = insert_sort(insert_sort_list)
    end = time()
    print(end-begin)
    #print(insert_sort_list_result)
    begin = time()
    merge_sort_list_result = merge_sort(merge_sort_list)
    end = time()
    print(end-begin)
    #print(merge_sort_list_result)

run()
