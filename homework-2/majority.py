"""
CSCI-665-01 Homework-2(majority.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program take n numbers from users and calculates if there exist an
element which occurs a.) n/2 times b.) n/3 times

Usage: python3 majority.py
n
numbers
"""
import random
import math
"""
Take n elements from user.
Randomly select any value from numbers
Iterate through the values and partition in three buckets Less,Equal & Greater
Less : This bucket will have all values less than pivot.
Equal : This bucket will have all values equal to pivot.
Greater : This bucket will have all values greater than pivot.
Compare searching index 'k' as follows:
if k is less than length(Less) then element is within Less Bucket and call
select with Less and k.
if k is greater length(Less) and k is less length(Less)+length(Equal) then 
we have found the element i.e pivot.
else element is in greater bucket and select only greater bucket as data 
and new k value i.e k-length(Less)-1,
The result of Select function is length of Equal bucket. The length of equal 
is checked compared to n/2 to find whether there exist element which occurs 
more than n/2.
if length is greater than n/2 then o/p is Yes.

"""
def Select(data,k):
    #if len less than 1 return
    if len(data) < 1:
        return
    #compute random pivot value
    #complexity O(n)
    pivot = data[random.randint(0,(len(data)-1))]
    #buckets to compare against pivot
    Less =[]
    Equal=[]
    Greater=[]
    '''
    The loop partition data into 3 buckets and store value
    less,equal,greater with respect to pivot in the bucket.
    Complexity : O(n)
    '''
    for index in range(len(data)):
        #to store
        if data[index] < pivot:
            Less.append(data[index])
        elif data[index] > pivot:
            Greater.append(data[index])
        else:
            Equal.append(data[index])
    '''
    Compare index to length of less if index within that range
    then value is in Less Bucket and compute select on that bucket.
    if value greater than less and within less and equal bucket then
    we have found value as pivot and return length of equal bucket
    else element in greater bucket compute select on greater bucket.
    '''
    if k < len(Less):
        return Select(Less,k)
    elif (k >=len(Less) and k < (len(Less) + len(Equal))):
        return len(Equal)
    else:
        return Select(Greater,k-len(Less)-len(Equal))
'''
The main function takes i/p from user and calls select function
for find index element at index a.) n//2 and b.) n//3
The result of select function is the count of the element at n//2 index 
in array.The result is used to find whether element occurs more than n//2 times.
Same Logic is for n//3 
'''
def main():
    #take i/p from user
    n = int(input())
    numbers = [int(x) for x in input().split(" ")]
    #complexity of select - O(n)
    count_2 = Select(numbers, n // 2)
    count_3 = Select(numbers, n // 3)
    #check if element is more than n//2 times
    if count_2 > n // 2:
        print("YES")
    else:
        print("NO")
    #check if element is more than n//3 times
    if (count_3 > n // 3):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()



