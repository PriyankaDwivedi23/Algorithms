"""
CSCI-665-01 Homework-3(donut.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The following code takes coordinate points (intersection )as input
and calculates the nearest intersection among the points given i.e.
intersection which will be close to rest of the intersections
"""

import sys
import math
import random

def main():
    """  Main Function to  take inputs and put it in array.
    """
    nPoints = int(input())

    points = []

    x=[]
    y=[]
    # Reading in the points
    n=nPoints
    for i in range(int(nPoints)):
        coordinates = input().split(" ")
        points.append([int(coordinates[0]), int(coordinates[1])])
        x.append(int(coordinates[0]))
        y.append(int(coordinates[1]))

    sum_x = Select(x, (n - 1) / 2)
    sum_y = Select(y, (n - 1) / 2)

    point_common = [math.floor(sum_x[0]), math.floor(sum_y[0])]
    print(calculateTotalDistance(points,point_common))




def calculateTotalDistance(list_points,point_common):
    """  Function to calculate the total distance of
        all intersections from the closest intersection
        @:param  list_points: list of all points
        @:param  point_common: closest point to all intersections
        @return sum: total distance
    """
    sum=0
    for s in list_points:
        sum=sum+calculateDistanceBetweenTwoPoints(s,point_common)
    return sum


def calculateDistanceBetweenTwoPoints(point1,point2):
    """  Function to calculate the  distance of
           two intersections
            @:param  point1: first intersection
            @:param  point2: second intersection
            @return x+y: total distance
        """
    x=abs(point1[0] - point2[0])
    y=abs(point1[1] - point2[1])
    return (x+y)


def Select(data,k):
    """
    Assume random value generated as pivot is good.
    (a)Take n elements from user.
    (b) Randomly select any value from numbers
    (c) Iterate through the values and partition in three buckets Less,Equal and Greater
    i. Less : This bucket will have all values less than pivot.
    ii. Equal : This bucket will have all values equal to pivot.
    iii. Greater : This bucket will have all values greater than pivot.
    (d) Compare searching index ’k’ as follows:
    if k is less than length(Less) then element is within Less Bucket and call select with Less and k.
    if k is greater length(Less) and k is less length(Less)+length(Equal) then we have found the element i.e pivot.
    else element is in greater bucket and select only greater bucket as data and new k value i.e k-length(Less)-1
    (e) The result is median value of co-ordinates
    Overall Complexity : O(n)


    :param data: co-ordinates
    :param k: median value
    :return: median of co-ordinates
    """
    if len(data) < 1:
        return
    x = len(data)-1
    pivot = data[random.randint(0,x)]

    Less =[]
    Equal=[]
    Greater=[]

    for index in range(len(data)):
        if data[index] < pivot:
            Less.append(data[index])
        elif data[index] > pivot:
            Greater.append(data[index])
        else:
            Equal.append(data[index])

    if k < len(Less):
        return Select(Less,k)
    elif (k >=len(Less) and k < (len(Less) + len(Equal))):
        return (Equal)
    else:
        return Select(Greater,k-len(Less)-len(Equal))

if __name__ == "__main__":
    main()