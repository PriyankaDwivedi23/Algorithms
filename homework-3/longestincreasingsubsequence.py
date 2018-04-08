"""
CSCI-665-01 Homework-5(longestIncreasingSubseqRecursive.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program take n numbers from users and calculate longest Increasing
 Subsequence using recursive method

Usage: python3 longestIncreasingsubsequence.py
n
numbers
"""
import sys

'''
The main function takes n input and perform longest Increasing subsequence.

'''
def main():
    n = int(input())
    sequence = [int(x) for x in input().split(" ")]
    print(longestIncreasingSubsequence(sequence))


def longestIncreasingSubsequence(sequence):
    '''
    Algorithm:
    1. Initialize dp array as 1 with size equal to length of sequence
    2. compute the value in dp array by considering to include or exclude that element
    3. For every j th element  iterate from that value till from 0 to j and check whether
    element is part of increasing sequence by using previously computed values in dp array.

    Overall complexity is O(n^2)

    @:param sequence - input sequence
    @:return length of increasing subsequence for sequence.
    '''
    dp_array = [1]*len(sequence)
    #consider every element
    for i in range(1, len(dp_array)):
        #initial len = 0
        len_lis = 0
        #consider previous element and check whether to include or exclude the element.
        for j in range(0, i):
            if (sequence[i] > sequence[j] and dp_array[i] < 1 + dp_array[j]):
                len_lis = max(len_lis,dp_array[j])
                dp_array[i] = len_lis + 1

    return max(dp_array)

if __name__ == '__main__':
    main()