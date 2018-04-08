"""
CSCI-665-01 Homework-4(parenthesesGreedy.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input the sequence of algebraic expressions
 and  determines the maximum possible value
that can be obtained from the expression by fully parenthesizing it.

"""



def main():
    """  Main Function to  take inputs and put it in array.
    """
    n = (input())
    seq = []

    coordinates = n.split(" ")
    for i in coordinates:
        seq.append((i))

    final=[]

    final=getFinalSeq(seq)


    sum=1
    for f in final:
        sum=sum*f
    print(sum)




def getFinalSeq(seq):
    """  Function to put numbers into stack and determine the highest possible value
    @:param seq:- sequence of algebraic expression

    @return  new_list :-list of numbers which has all the numbers which have to be
    multiplied to get the highest value
       """
    new_list=[]
    i=0
    while(i<len(seq)):


        sum=0
        if(seq[i]=="*"):
            i=i+1

        elif(seq[i]=="+")  :
            sum=new_list.pop()
            sum=int(sum)+int(seq[i+1])
            new_list.append(sum)
            i=i+2

        else:

            new_list.append(int(seq[i]))
            i = i + 1

    return new_list


if __name__ == '__main__':
        main()
