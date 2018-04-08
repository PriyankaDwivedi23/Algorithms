"""
CSCI-665-01 Homework-3(doubleKnapsack.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input of weight and cost associated with the weight.
The program computes the maximum cost that can be gained by filling
two bags by using the weights given by user.
Usage : python3 doubleKnapsack.py
n W1 W2
weight cost

"""

def double_knapsack():
    '''
    For every item
    Calculate
    1. Cost if j element is considered
    2. Cost if weight is accomodated in bag 1
    3. Cost if weight is accomodated in bag 2
    If both bags have places then max between above 3 is taken.
    If weight can be accomodated in bag 1 the max of 1 and 2 is taken.
    If weight can be accomodated in bag 2 the max of 1 and 3 is taken.

    After all items are considered return knapsack[W1][W2]
    :return: maximum cost for filling bag 1 and 2 using given weight
    '''
    n,W1,W2 = [int(x) for x in input().split(" ") ]
    #initialize knapsack to 0
    knapsack = [[0 for k in range(W1+1)] for j in range(W2+1)]
    for item in range(n):
        #consider each item
        weight, cost = [int(x) for x in input().split(" ")]
        for w1 in range(W1,-1,-1):
            for w2 in range(W2,-1,-1):
                #if both bags have capacity consider one with high cost
                if (w1 >= weight and w2 >= weight):
                    knapsack[w1][w2] = max( knapsack[w1][w2] ,  knapsack[w1-weight][w2] + cost , knapsack[w1][w2-weight]+cost)
                #if bag 1 has capacity consider max of either including or excluding
                elif (w1 >= weight):
                    knapsack[w1][w2] = max(knapsack[w1][w2], knapsack[w1 - weight][w2] + cost )
                # if bag 2 has capacity consider max of either including or excluding
                elif (w2 >= weight):
                    knapsack[w1][w2] = max(knapsack[w1][w2],knapsack[w1][w2 - weight] + cost)

    return knapsack[W1][W2]



if __name__ == '__main__':
    print(double_knapsack())

