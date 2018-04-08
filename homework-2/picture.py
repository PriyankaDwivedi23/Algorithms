"""
CSCI-665-01 Homework-2(picture.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program take n i.e number of student and 1 teacher in the picture.
There are 7 year old student which should be placed first according to
increasing order of their height and after that the Teacher will stand
followed by 8 year old students in decreasing order of their height.

Usage: python3 picture.py
n
age height
"""
"""
Algorithm:
We use divide and conquer technique to solve the problem.
Step 1: Divide
Divide the data into halves recursively until single element is left
Time Complexity O(logn)
Step 2: Conquer
Since data is divided into half each time we end up having left and
right. This step we make the count of swap to be done to bring the 
element at its correct position.
Overall complexity is 0(n) to merge the data.
Step 3: Combine
The swap count for all the step is combined to give final swap count
that will be performed to allign student and Professor as per the
instruction by photographer.
Overall complexity :
1. Divide - O(logn)
2. Merge - O(n) We merge logn times 
Therefore overall Complexity O(nlogn)
"""


'''
The function will divide the list into half which takes complexity
of O(logn) and n items iterated log(n) times gives O(n log(n)).
@:param data : List of students and Teacher
@:return merged list and count of swaps 
'''
def divide(data):
    #if only single element remains return element and count
    count = 0
    if len(data) < 2:
        return data,count
    #divide in two half
    left, left_count = divide(data[:len(data) // 2])
    right,right_count =  divide(data[len(data) // 2:])
    #merged the half
    merged, count = conquer(left, right)
    #calculate the swap count
    count += (left_count + right_count)

    return merged,count
'''

The function take left of the split and right of split and merges them.
However there are some condition for sorting.
If both left and right element is a student of 7 year we sort according to
height i.e ascending order of height.
If both left and right element is a student of 8 year we sort according to
height i.e descending order of height.
If left is 7 year student and right is 8 year then 7 year student will stand
first.
If left is 7 year student and right is Professor then 7 year student will 
stand first.
If left is 8 year student and right is Professor then Professor will stand 
first.
Merge the list according to these condition so that students and teacher allign
according to instruction by photographer.
While merging we keep track of swap count using counting inversion.
Overall Complexity turns out to be O(nlogn) 

@:param lefthalf - leftside of half
@:param righthalf - rightside of half
@:return merged and sorted list of lefthalf and right half and swap count
'''
def conquer(left, right):
    # stores the result
    list = []
    #index pointers to compare elements
    leftindex,rightindex = 0,0
    #stores the swap count
    swap_count = 0
    #compares the value and merges the element
    '''
    The loop runs until either of pointer have reached the end of halves.
    leftindex is pointer for left and rightindex pointer for right
    Compare the values of the element at that pointers and append to result
    with update on swap count.The element added in result has its index pointer
    incremented by 1.We continue to compare until either pointer runs out of
    index.
    '''
    while leftindex < len(left) and rightindex < len(right):
    #left element = 7 and right element = 7 comapre height according to height
        if left[leftindex][0] == 7 and right[rightindex][0] == 7:
            #compare height
            if left[leftindex][1] < right[rightindex][1]:
                list.append(left[leftindex])
                leftindex +=1
            else:
                list.append(right[rightindex])
                rightindex+=1
                swap_count += len(left) - leftindex
    # left element = 8 and right element = 8 comapre height according to height
        elif left[leftindex][0] == 8 and right[rightindex][0] == 8:
            #compare height
            if left[leftindex][1] < right[rightindex][1]:
                list.append(right[rightindex])
                rightindex +=1
                swap_count += len(left) - leftindex
            else:
                list.append(left[leftindex])
                leftindex+=1
    # left element = Professor compare right element
        elif left[leftindex][0] > 8  :
            #right element = 7 append 7 to list
            if right[rightindex][0] == 7:
                list.append(right[rightindex])
                rightindex+=1
                swap_count += len(left) - leftindex
            #right element = 8 append professor
            else:
                list.append(left[leftindex])
                leftindex += 1
    #right element = Professor compare left element
        elif right[rightindex][0] > 8  :
            #if left = 7 append student
            if left[leftindex][0] == 7:
                list.append(left[leftindex])
                leftindex+=1
            #else left = 8 append professor
            else:
                list.append(right[rightindex])
                rightindex += 1
                swap_count += len(left) - leftindex
    #if both left and right are different i.e 7 year and 8 year
    #student comparison will append 7 year student.
        elif left[leftindex][0] < right[rightindex][0]:
            list.append(left[leftindex])
            leftindex+=1
        else:
            list.append(right[rightindex])
            rightindex+=1
            swap_count += len(left) - leftindex

    #Append the remaining element in left or right to the result
    if leftindex < len(left):
        list.extend(left[leftindex:])
    elif rightindex < len(right):
        list.extend(right[rightindex:])

    return list,swap_count

'''
The main function take inputs from users and
calls divide method which splits the students and merges according to
desired output

'''
def main():
    #n-number of people in picture
    #O(1)
    n = int(input())
    #stores [age,height] of student and teacher
    people = []
    '''
    The loop takes age and height of student and teacher and 
    append in list of list format.
    runs n times
    Time Complexity - O(n)
    '''
    for _ in range(n):
        age, height = [x for x in input().split(" ")]
        people.append([int(age), float(height)])
    #calls divide method to get swap count
    #complexity O(nlogn)
    sorted_list, swap_count = divide(people)
    #print swap count
    print(swap_count)



if __name__ == '__main__':
    main()
