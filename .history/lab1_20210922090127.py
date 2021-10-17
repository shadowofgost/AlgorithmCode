"""
Author: Zirui Wang
Date: 2021-09-21 18:13:25
LastEditTime: 2021-09-22 08:55:27
LastEditors: Please set LastEditors
Description: First lab
FilePath: \AlgorithmCode\lab1.py
"""


def insert_sort(initial_list):
    """
    插入排序

    Args:
        initial_list (list): 初始数据列表

    Returns:
        list: 结果数据列表
    """
    length = len(initial_list)
    for i in range(length):
        if i <= 1:
            return initial_list
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
    result_list = []
    return result_list
