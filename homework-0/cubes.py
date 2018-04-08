"""
CSCI-665-01 Homework-0(cubes.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)

The program takes input from user and prints out in increasing order,
starting from 0, all positive perfect cubes less than or equal to that value.

Usage: python3 cubes.py
number

"""

def main():
    number = 0
    # validation for positive number
    while(True):
        number = int(input())
        if number > 0:
            break
        else:
            print("Enter only positive number")

    i , cube = 1,0
    '''
    The loop run until cube of number is less than or equal to user input.
    It print all the cube until condition is false.
    '''
    while( cube <=  number):
        print(cube)
        cube = i**3
        i +=1


if __name__ == '__main__':
    main()