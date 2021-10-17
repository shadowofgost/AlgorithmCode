"""
Author: Zirui Wang
Date: 2021-09-21 18:13:25
LastEditTime: 2021-09-22 08:55:27
LastEditors: Please set LastEditors
Description: First lab
FilePath: \AlgorithmCode\lab1.py
"""

#from matplotlib import pyplot as plt
from random import randint
from time import time
from copy import copy, deepcopy
from numpy import mean
from multiprocessing import Pool


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

    def merge(s1, s2, s):
        """将两个列表是s1，s2按顺序融合为一个列表s,s为原列表"""
        # j和i就相当于两个指向的位置，i指s1，j指s2
        i = j = 0
        length = len(s)
        while i + j < length:
            # j==len(s2)时说明s2走完了，或者s1没走完并且s1中该位置是最小的
            if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                s[i + j] = s1[i]
                i += 1
            else:
                s[i + j] = s2[j]
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
    merge(s1, s2, initial_list)
    return initial_list
'''
def test_insert_sort_single(initial_list):
    begin = time()
    insert_sort(initial_list)
    end = time()
    return end - begin


def test_insert_sort_once(initial_list):
    """
    计算每次n，10次情况下的平均值

    Args:
        initial_list ([type]): [description]

    Returns:
        [type]: [description]
    """
    pools_once = Pool(len(initial_list))
    result = pools_once.map(test_insert_sort_single, initial_list)
    pools_once.join()
    return mean(result)
'''
def test_insert_sort_once(initial_list):
    tmp_time_list = []
    for i in range(len(initial_list)):
        initial_list[i] = list(initial_list[i])
        begin = time()
        insert_sort(initial_list[i])
        end = time()
        tmp_time_list.append(end - begin)
    return mean(tmp_time_list)



def test_insert_sort(initial_list):
    insert_sort_list = deepcopy(initial_list)
    for i in range(len(insert_sort_list)):
        '''
        for j in range(len(insert_sort_list[i])):
            insert_sort_list[i][j] = tuple(insert_sort_list[i][j])
        insert_sort_list[i] = tuple(insert_sort_list[i])
        '''
    pools = Pool(len(insert_sort_list))
    result = pools.map(test_insert_sort_once, insert_sort_list)
    pools.close()
    pools.join()
    return result


def test_merge_sort(initial_list):
    merge_sort_list = deepcopy(initial_list)
    time_list = []
    for i in merge_sort_list:
        tmp_time_list = []
        for j in i:
            begin = time()
            merge_sort(j)
            end = time()
            tmp_time_list.append(end - begin)
        time_list.append(mean(tmp_time_list))
    return time_list


def run():
    n_list = [10000, 20000, 30000, 40000, 50000]
    initial_list = [
        [[randint(0, n_list[k]) for i in range(n_list[k])] for j in range(10)]
        for k in range(len(n_list))
    ]
    begin = time()
    merge_sort_time_result = test_merge_sort(initial_list)
    end = time()
    print(end - begin)
    print(merge_sort_time_result)
    begin = time()
    insert_sort_time_result = test_insert_sort(initial_list)
    end = time()
    print(end - begin)
    print(insert_sort_time_result)


def test():
    n_list = [10000, 20000, 30000, 40000, 50000]
    initial_list = [
        [[randint(0, n_list[k]) for i in range(n_list[k])] for j in range(10)]
        for k in range(len(n_list))
    ]
    insert_sort_initial_list = deepcopy(initial_list[0][0])
    merge_sort_initial_list = deepcopy(initial_list[0][0])
    begin = time()
    merge_sort_time_result = merge_sort(merge_sort_initial_list)
    end = time()
    print(end - begin)
    print(merge_sort_time_result)
    begin = time()
    insert_sort_time_result = insert_sort(insert_sort_initial_list)
    end = time()
    print(end - begin)
    print(insert_sort_time_result)
if __name__ == "__main__":
    run()
    #test()
[0.11930041313171387, 0.48359973430633546, 1.0410563230514527, 1.2678932189941405, 2.6394350051879885]
