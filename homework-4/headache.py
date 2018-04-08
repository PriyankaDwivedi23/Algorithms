"""
CSCI-665-01 Homework-4(pathInMaze.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program
Usage: python3 headache.py
number of people in line 1
number of people in line 2
line1
line2
"""
def match_sameLine(val1,val2):
    '''
    The function returns 5 if E and N are paired together else return 3
    :param val1: person 1
    :param val2: person 2
    :return: headache caused to ride two persons
    '''
    if val1 != val2:
        if (val1 == 'E' and val2 == 'N') or (val1 == 'N' and val2 == 'E'):
            return 5
    return 3

def match_differentLine(val1,val2):
    '''
    The function returns 5 if E and N are paired together else return 0
    :param val1: person 1
    :param val2: person 2
    :return: headache caused to ride two persons
    '''
    if val1 != val2:
        if (val1 == 'E' and val2 == 'N') or (val1 == 'N' and val2 == 'E'):
            return 5
    return 0

def cal_headache(line1,line2,match_EN,single_person,match_sameline):
    '''
    The function calculates minimum headache caused to take line1 and line2 for ride
    where following condition apply
    1. matching E and N gives headache of 5 others as 0.
    2. matching two people from same line is 3 or 5 if E and N otherwise 0 if other
    line is empty.
    3.Sending single person causes headache of 4.
    :param line1: persons in line 1
    :param line2: persons in line 2
    :param match_EN: headache caused to pair E and N
    :param single_person: headache caused to send single person
    :param match_sameline: headache caused to send two people from same line
    :return: minimum headache caused by sending line1 and line2
    Complexity : O(mn)
    '''
    #initialise headache to 0 for all
    headache = [[0 for i in range(len(line2) + 1)] for j in range(len(line1) + 1)]
    #initialise row and col
    row  = 0
    col =0
    #compute headache
    for row in range(len(line1)+1):
        for col in range(len(line2)+1):
            #base case if row ==0 check cost to send single person and send two person from same line
            #take minimum of two values
            if row == 0:
                if  col-1 > 0:
                    match_pair = match_differentLine(line2[col-1],line2[col-2])
                    headache[row][col]= min(single_person+headache[row][col-1],match_pair+headache[row][col-2])
            # base case if col ==0 check cost to send single person and send two person from same line
            # take minimum of two values
            elif col == 0:
                if row - 1 > 0:
                    match_pair = match_differentLine(line1[row - 1], line1[row - 2])
                    headache[row][col] = min(single_person + headache[row-1][col],match_pair + headache[row-2][col])
            #check value for sending single person from both line, send one person from each line,
            #send two persons from same line and use minimum value among that.
            elif col-1 >= 0 and row-1 >= 0:
                match_pair = match_differentLine(line1[row-1],line2[col-1])
                headache[row][col] = min(single_person+headache[row-1][col], single_person+headache[row][col-1],match_pair+headache[row-1][col-1])
                if col-2 >=0:
                    match_pair = match_sameLine(line2[col-1],line2[col-2])
                    headache[row][col] = min(headache[row][col] , match_pair + headache[row][col-2])
                if row-2 >=0:
                    match_pair = match_sameLine(line1[row - 1], line1[row - 2])
                    headache[row][col] = min(headache[row][col],match_pair + headache[row-2][col])

    return headache[row][col]

def main():
    '''
    Take input from user and calculate the minimum headache that will be cost
    to ride people in line 1 and line 2.
    '''
    m = int(input())
    n = int(input())
    line1 =[ x for x in input().split(" ")]
    line2=[x for x in input().split(" ")]
    #headache incurred when E and N are paired
    match_EN = 5
    # headache incurred when single person take ride
    match_singleperson = 4
    # headache incurred when two people from same line are taken
    match_sameline = 3
    #calculate headache
    print(cal_headache(line1, line2 , match_EN,match_singleperson,match_sameline))



if __name__ == '__main__':
    main()

