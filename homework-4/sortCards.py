"""
CSCI-665-01 Homework-1(sortCards.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program take n numbers from users compute minimum number of moves
required to sort the n elements

Usage: python3 sortCards.py
n
numbers
"""
import sys

'''
The main function takes n input and perform longest Increasing subsequence 
which gives length of longest common subsequence. Since we know the length of 
common subsequence we know that these number are in ascending order and we need to
move only those numbers which are in between the subsequence which will make move 
of length of sequence - length of longest common subsequence which will return the
minimum number of moves to moves those elements.

'''
def main():
    #take input from user
    n = int(input())
    #take sequence from user
    sequence = [int(x) for x in input().split(" ")]
    #compute the length of common subsequence
    longest_common_subsequence = longestIncreasingSubsequence(sequence)
    #compute the minimum moves
    min_moves = getMinimumMoves(longest_common_subsequence,len(sequence))
    print(min_moves)


def getMinimumMoves(longest_common_subsequence,length_sequence):
    '''
    The function returns the minimum number of moves required to sort the
    elements by subtracting longest common subsequence from length of
    subsequence since longest common sequence are already in ascending
    order we need to move only those elements that are in between the longest
    common subsequence.
    complexity  : O(1)


    :param longest_common_subsequence: length of longest common subsequence
    :param length_sequence: length of subsequence
    :return: minimum moves to sort the numbers
    '''
    min_moves =  length_sequence-longest_common_subsequence
    return min_moves

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
            if (sequence[i] > sequence[j] and dp_array[i] < 1 +dp_array[j]):
                len_lis = max(len_lis,dp_array[j])
                dp_array[i] = len_lis + 1

    return max(dp_array)

if __name__ == '__main__':
    main()