#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    N = 5
    # input data
    print '请输入10个数字:\n'
    l = []
    for i in range(N):
        l.append(int(raw_input('输入一个数字:\n')))
    print    #只输出了一个空行，与下面的代码没有直接关联
    for i in range(N):
        print l[i]
    print

    # 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if l[min] > l[j]: min = j
        l[i], l[min] = l[min], l[i]
    print '排列之后：'
    for i in range(N):
        print l[i]