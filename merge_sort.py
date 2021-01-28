#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import random

def gen_list(nums):
    res = range(nums)
    random.shuffle(res)
    return res


def merge(left , right):
    tmp_res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp_res.append(left[i])
            i = i +1
        else:
            tmp_res.append(right[j])
            j = j +1
    tmp_res += left[i:]
    tmp_res += right[j:]
    return tmp_res

#默认从小到大排序
def merge_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list

    mid = len(sort_list) / 2
    left = merge_sort(sort_list[:mid])
    right = merge_sort(sort_list[mid:])

    return merge(left , right)

if __name__ == '__main__':
    nums = 20
    sort_list = gen_list(nums)
    print sort_list
    sort_list = merge_sort(sort_list)
    print sort_list
    pass
