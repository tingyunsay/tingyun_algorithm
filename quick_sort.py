#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import random

def gen_list(nums):
    res = range(nums)
    random.shuffle(res)
    return res

#默认从小到大排序
def quick_sort(sort_list,begin,end):
    if len(sort_list) <= 1 or begin > end:
        return sort_list
    left = begin
    right = end
    #保存第一个元素的值，一次快排后处于自己的位置（排好序的位置）
    temp = sort_list[left]
    while left < right:
        while (left < right) and (sort_list[right] > temp):
            right -= 1
        sort_list[left] = sort_list[right]
        while (left < right) and (sort_list[left] < temp):
            left += 1
        sort_list[right] = sort_list[left]
    print sort_list,"----"
    sort_list[left] = temp
    print sort_list,"----"
    quick_sort(sort_list,begin,left-1)
    quick_sort(sort_list,right+1,end)
    pass

#begin和end 默认应为元素下标 最大和最小值
def quick_sort_2(sort_list,begin,end):
    if len(sort_list) <= 1 or begin > end:
        return sort_list
    i = begin
    j = end
    temp = sort_list[i]
    while i < j:
        #第一个小于temp的数
        while (i<j) and (sort_list[j] > temp):
            j -= 1
        #第一个大于temp的数，跳过自身
        while (i<j) and (sort_list[i] <= temp):
            i += 1
        #交换两个数的值
        tmp = sort_list[i]
        sort_list[i] = sort_list[j]
        sort_list[j] = tmp
    #交换最后一个j 和temp的值
    sort_list[begin] = sort_list[j]
    sort_list[j] = temp
    #从j这个位置左右两边递归
    quick_sort_2(sort_list, begin, j -1 )
    quick_sort_2(sort_list, j +1, end)



if __name__ == '__main__':
    nums = 20
    sort_list = gen_list(nums)
    #sort_list = [0, 3, 9, 1, 6, 4, 5, 8, 7, 2]
    print sort_list
    quick_sort_2(sort_list,0,len(sort_list)-1)
    print sort_list
    pass

    #注：两种不同的交换两个元素的实现，第一个理解起来麻烦一点，第二个比较好理解