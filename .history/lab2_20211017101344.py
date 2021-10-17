'''
Author: Albert Wang
LastEditors: Albert Wang
Date: 2021-10-17 08:37:42
LastEditTime: 2021-10-17 10:12:53
Description:lab2
FilePath: \\AlgorithmCode\\lab2.py
Copyright Notice:  2021 Albert Wang 王子睿.All Rights Reserved.
'''

def RunningTime(func):
    def test(n):
        from time import time
        start = time()
        result = func(n)
        end = time()
        print(result,end-start)
    return test

@RunningTime
def Gray(n):
    if n == 1:
        return ['0','1']
    else:
        list_result = []
        a = Gray(n-1)
        for i in a:
            list_result.append('0'+i)
        for i in a[::-1]:
            list_result.append('1'+i)
        return list_result


def test():
    for i in range(1,10):
        Gray(i)

if __name__ == '__main__':
    test()
    