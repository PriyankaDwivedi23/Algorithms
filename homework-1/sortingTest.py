"""
CSCI-665-01 Homework-1-5(sortingTest.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input from user and sorts the input using
merge sort,insertion sort and bucket sort

Usage: python3 sortingTest.py
unsorted numbers to perform merge and insertion sort
unsorted number to perform bucket sort

"""

import math
import random as r
import time as t

'''
The function performs insertion sort as follows:
1.Iterate loop from start to end.
2.Pick element and insert into sorted sequence from 
index 0 till current value (index-1).

@:param  : unsorted list
@:return : sorted list

Complexity : O(n^2)
'''
def insertion_sort(sorting_list):
    # if single element then return
    if len(sorting_list) <= 1:
        return sorting_list
    #consider 2nd element as we consier first element to be sorted
    i = 1
    #loop takes the current value and checks with left sorted values
    #and places on right position
    #complexity : O(n^2)
    while i < len(sorting_list):
        currentValue = sorting_list[i]
        index = i - 1
        while index >= 0 and sorting_list[index] > currentValue:
            sorting_list[index + 1] = sorting_list[index]
            sorting_list[index] = currentValue
            index -= 1
        i += 1
    return sorting_list



'''
The function performs merge sort using helper function merge_sort as following:
1.Base case : If length of unsorted list less then 2 then return list
2.Iterate through list and break it into two equal half.
3.Spilt until broken into single element.
4.Start merging the half in sorting order.

@:param : unsorted list
@:return: sorted list

Complexity : O(nlogn)

'''

# Splits the array and perform merge sort on two halfs
def mergeSort(data):
    #if only single element remains return element
    if len(data) < 2:
        return data
    else:
    #spilt the array into two parts
        left, right = data[:len(data) // 2], data[len(data) // 2:]

    return merge_sort(mergeSort(left), mergeSort(right))

#merge the two half
def merge_sort(left, right):
    result = []
    leftindex, rightindex = 0, 0
    #compares the value and merges the element
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] <= right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    #checks for remaining value if any append to result
    if leftindex < len(left):
        result.extend(left[leftindex:])
    elif rightindex < len(right):
        result.extend(right[rightindex:])

    return result

'''
The below function is bucket sort. In this we create n empty buckets 
(Or lists) and insert each element from the array to be sorted into buckets 
at n*arr[i] index positions.Then insertion sort is used to sort 
individual buckets used and then all buckets are concatenated into a new array


'''
def bucket_sort(sorting_list):
    #create bucket of size 10
    buckets = [[] for x in range(10)]
    #add into bucket according to value
    for element, x in enumerate(sorting_list):
        buckets[int(x * len(buckets))].append(x)
    output = []
    #merge each bucket us
    for bucket in buckets:
        output += insertion_sort(bucket)
    return output



'''
The main function takes input from user for n and
unsorted number.Perform insertion sort,merge sort and bucket sort 
on unsorted list and compare the running time of below sort with 
different size of input.

'''


def main():
    print("Enter value to sort using Merge and Insertion sort with spaces:")
    unsorted_list = [int(x) for x in input().split(" ")]

    print("Using Merge Sort: ", mergeSort(unsorted_list))
    print("Using Insertion Sort: ", insertion_sort(unsorted_list))
    print("Enter values for bucket sort with spaces:")
    bucketsort = [float(x) for x in input().split(" ")]
    print("Using Bucket Sort: ", bucket_sort(bucketsort))

if __name__ == '__main__':
    main()