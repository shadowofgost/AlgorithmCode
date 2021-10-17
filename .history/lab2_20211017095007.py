'''
Author: Albert Wang
LastEditors: Albert Wang
Date: 2021-10-17 08:37:42
LastEditTime: 2021-10-17 09:49:27
Description:lab2
FilePath: \\AlgorithmCode\\lab2.py
Copyright Notice:  2021 Albert Wang 王子睿.All Rights Reserved.
'''
def Gray(n):
    if n == 1:
        return ['0','1']
    else:
        list_result = []
        a = Gray(n-1)
        for i in a:
            list_result.append('0'+i)
        for i in a[-1:0]:
            list_result.append('1'+i)
        return list_result

def RunningTime(func):
    def wrapper




    
def test():
    from time import time
    start = time()
    end
