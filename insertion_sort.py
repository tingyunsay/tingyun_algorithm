#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import random

def gen_list(nums):
    res = range(nums)
    random.shuffle(res)
    return res

#默认从小到大排序
def insertion_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    for i in range(len(sort_list)):
        for j in range(i,len(sort_list)):
            if sort_list[i] > sort_list[j]:
                tmp = sort_list[i]
                sort_list[i] = sort_list[j]
                sort_list[j] = tmp
        #没一趟排序的结果
        print sort_list
    pass


if __name__ == '__main__':
    nums = 20
    sort_list = gen_list(nums)
    print sort_list
    insertion_sort(sort_list)
    print sort_list
    pass