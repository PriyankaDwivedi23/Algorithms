"""
CSCI-665-01 Homework-0(evensum.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)

The program take n numbers from user and prints sum of even integer

Usage: python3 evensum.py
n
n consecutive number
"""
def main():
    n = int(input())
    sum = 0
    count=0
    '''
    The loop continue until n consecutive are taken from user and
    calculates the sum of only even integers
    '''
    while(count<n):
        i = int(input())
        # validate for positive number
        if(i<0):
            print("Please Enter only Positive number ")
            continue
        if(i%2 ==0):
            sum += i
        count+=1
    # prints the sum
    print(sum)

if __name__ == '__main__':
    main()