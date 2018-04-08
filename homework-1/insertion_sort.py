"""
CSCI-665-01 Homework-1-5(sortingTest.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input from user and sorts the input using
merge sort,insertion sort and bucket sort

Usage: python3 sortingTest.py
number of elements to be sorted
unsorted numbers

"""

import math

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
    #iterate through list

    for i in range(1, len(sorting_list)):
        #get current value
        currentvalue = sorting_list[i]
        index_position = i
        #put current element into sorted sequence
        while(sorting_list[index_position - 1] > currentvalue and index_position > 0):
            sorting_list[index_position] = sorting_list[index_position - 1]
            index_position = index_position - 1
        sorting_list[index_position] = currentvalue
    return (sorting_list)

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
def mergeSort(data):
    if len(data) < 2 :
        return data
    else:
        left , right = data[:len(data)//2] , data[len(data)//2:]

    return merge_sort(mergeSort(left),mergeSort(right))

def merge_sort(left,right):
    result = []
    leftindex , rightindex =0,0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] <= right[rightindex]:
            result.append(left[leftindex])
            leftindex +=1
        else:
            result.append(right[rightindex])
            rightindex +=1

    if leftindex < len(left):
        result.extend(left[leftindex:])
    elif rightindex < len(right):
        result.extend(right[rightindex:])

    return result

'''
The above function performs bucket sort as follows:
'''
def sortArray(sorting_list, n ):
    bucket_size = 10
    bucket = []


'''
The main function takes input from user for n and
unsorted number.Perform insertion sort,merge sort and bucket sort 
on unsorted list and compare the running time of below sort with 
different size of input.
 
'''
def main():
    n = int(input())
    sorting_list = [int(x) for x in input().split(" ")]
    print("Insertion Sort : ", end= ' ')
    print(insertion_sort(sorting_list))
    print("Merge Sort : ", end=' ')
    print(mergeSort(sorting_list))



if __name__ == '__main__':
    main()