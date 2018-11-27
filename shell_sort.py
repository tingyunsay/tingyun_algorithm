#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import random

def gen_list(nums):
    res = range(nums)
    random.shuffle(res)
    return res

#默认从小到大排序
def shell_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    size = len(sort_list)
    group = size / 2
    while group >= 1:
        #按照group的分组进行插入排序，group越到小，整个数组越接近于有序
        for i in range(len(sort_list)):
            while i < size and (i + group) < size:
                if sort_list[i] > sort_list[i+group]:
                    tmp = sort_list[i]
                    sort_list[i] = sort_list[i+group]
                    sort_list[i+group] = tmp
                i += group
        #每一趟排序的结果
        print sort_list
        group /= 2
    pass


if __name__ == '__main__':
    nums = 20
    sort_list = gen_list(nums)
    print sort_list
    shell_sort(sort_list)
    print sort_list
    pass