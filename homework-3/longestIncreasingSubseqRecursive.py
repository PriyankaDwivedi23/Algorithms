"""
CSCI-665-01 Homework-5(longestIncreasingSubseqRecursive.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program take n numbers from users and calculate longest Increasing
 Subsequence using recursive method

Usage: python3 longestIncreasingSubseqRecursive.py
n
numbers
"""
import sys


def longestIncreasingSubseqRecursive(sequence, previous_element, current_element):
    '''
    Algorithm:
    1. Base case if current position is end of sequence return 0
    2.Recursive Case:
    1. Start from index 0 and find lis for considering that element and lis for not
    considering that element.
    2. Maximum of both these will be returned.

    Over all complexity is  n * 2^n since for every element we have two option and we recursively
    calculate solution so n * 2^n size tree will be formed.

    @:param sequence         - sequence whose subsequence is to be find out
    @:param previous_element - stores the previous position for comparison
    @:param current_element  - stores the current position for comparison

    @:return length of longest increasing subsequence of given sequence
    '''


    n = len(sequence)
    # Base Case if reached end of sequence
    if (current_element == n):
        return 0
    # consider case where we include that item or exclude
    element_taken =  0
    # if current item greater than previous element then element taken will be 1 + lis for seq[j:]
    # where j is current element and we need to find sequence greater than current value.
    if (sequence[current_element] > previous_element):
        element_taken = 1 + longestIncreasingSubseqRecursive(sequence, sequence[current_element], current_element + 1)

    # if current element is not considered we find lis for seq[:j] and return max

    return max(element_taken, longestIncreasingSubseqRecursive(sequence, previous_element, current_element + 1))

'''
The main function takes n input and perform longest Increasing subsequence.
'''

def main():

    n = int(input())
    sequence = [int(x) for x in input().split(" ")]
    print(longestIncreasingSubseqRecursive(sequence,0,0))

if __name__ == '__main__':
    main()