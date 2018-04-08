import math
def Select_Median(data,k):
    partitions =[data[i:i+5] for i in range(0,len(data),5)]
    # print("Partition : " ,partitions)
    medians = []
    for partition in partitions:
        medians.append( sorted(partition)[len(partition)//2])
    # print(medians)

    if(len(medians) > 5):
        pivot = Select_Median(medians,len(medians)//2)
    else:
        pivot = sorted(medians)[len(medians)//2]

    # print("Pivot",pivot)
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
    #
    # print("Less",Less)
    # print("Equal",Equal)
    # print("Greater",Greater)
    # print("Need to find element at index",k)
    if k < len(Less):
        return Select_Median(Less,k)
    elif (k >=len(Less) and k < (len(Less) + len(Equal))):
        return pivot
    else:
        return Select_Median(Greater,(k-len(Less)))


if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split(" ")]
    # print(numbers)
    element_2 = Select_Median(numbers,math.ceil(n//2))
    element_3 = Select_Median(numbers,math.ceil(n/3))
    # print()
    count_2 = 0
    count_3 =0
    for number in numbers:
        if number == element_2:
            count_2 +=1
        if number == element_3:
            count_3 +=1
    # print("Count for n/3 ",count_3)
    if count_2 > n//2:
        print("YES")
    else:
        print("NO")
    if(count_3 > n//3):
        print("YES")
    else:
        print("NO")


