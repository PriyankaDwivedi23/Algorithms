"""
CSCI-665-01 Homework-4(parenthesesDP.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input the sequence of algebraic expressions
 and  determines the maximum possible value
that can be obtained from the expression by fully parenthesizing it.

"""

import math
def main():
    """  Main Function to  take inputs and put it in array.
    """

    n = (input())
    seq = []

    coordinates = n.split(" ")
    for i in coordinates:
        seq.append(i)

    numbers_list=[]
    sign_list=[]

    leng=len(seq)

    for g in range(len(seq)):

        if(g%2==0):
            numbers_list.append(int(seq[g]))
        else:sign_list.append(seq[g])


    parenAlgo(numbers_list,sign_list)


def parenAlgo(numbers_list,sign_list) :
    """  Function to put numbers matrix and find the different values by parenthesizing the sequence.
        In this ,first the elements or numbers are filled diagonally which will be the base case
        and the maximum and minimum is computed based on the symbols occurring in the sequence

        @:param numbers_list:- list of all the numbers in the given sequence
        @:param sign_list:- sequence of operators

    """
    dynamic =  [[[math.inf,None] for i in range(len(numbers_list))] for j in range(len(numbers_list))]
    i=0
    # loop for initializing the array (base case)
    for k in range(len(numbers_list)):
        for j in range(len(numbers_list)):
            if(k==j):
                dynamic[k][j]=[int(numbers_list[i]),int(numbers_list[i])]
                i+=1


    for d in range(0,len(numbers_list)):
        for L in range(0,len(numbers_list)-d):
            R = L + d
            # loop for finding the minimum
            for k in range(L,R):
                    sign=sign_list[k]
                    if(sign=='+'):
                        temp=eval(str(dynamic[L][k][0])+'+' +  str(dynamic[k+1][R][0]))
                        if(dynamic[L][R][0]==math.inf):
                            dynamic[L][R][0]=temp
                        elif(temp>(dynamic[L][R][0])):
                            dynamic[L][R][0]=temp
                    elif(sign=='-'):
                        temp=eval( str(dynamic[L][k][0]) +'-' + str(dynamic[k+1][R][1]) )
                        if (dynamic[L][R][0] == math.inf):
                            dynamic[L][R][0] = temp
                        elif (temp > (dynamic[L][R][0])):
                            dynamic[L][R][0] = temp
            # loop for finding the minimum
            for k in range(L,R):
                    sign=sign_list[k]
                    if(sign=='+'):
                        temp=eval(str(dynamic[L][k][1])+'+' +  str(dynamic[k+1][R][1]))
                        if (dynamic[L][R][1] == None):
                            dynamic[L][R][1] = temp
                        elif(temp<(dynamic[L][R][1])):
                            dynamic[L][R][1]=temp
                    elif(sign=='-'):
                        temp=eval(str(dynamic[L][k][1])+'-' + str(dynamic[k+1][R][0]))
                        if (dynamic[L][R][1] == None):
                            dynamic[L][R][1] = temp
                        elif (temp < (dynamic[L][R][1])):
                            dynamic[L][R][1] = temp

    # printing the maximum value of last row and first column
    print(dynamic[0][len(numbers_list)-1][0])


if __name__ == '__main__':
        main()