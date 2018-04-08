def mergeSort(data):
    #if only single element remains return element
    if len(data) < 2:
        return data
    else:
    #spilt the array into two parts
        left, right = data[:len(data) // 2], data[len(data) // 2:]

    return merge_sort(mergeSort(left), mergeSort(right))

#merge the two half
def merge_sort(left, right):
    result = []
    leftindex, rightindex = 0, 0
    #compares the value and merges the element
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] <= right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    #checks for remaining value if any append to result
    if leftindex < len(left):
        result.extend(left[leftindex:])
    elif rightindex < len(right):
        result.extend(right[rightindex:])

    return result



def WHATDOIDO( left,  right):
    A=[5,9,7,1,4,10]
    if left == right:
        return (1, 1, 1)
    else:
        m = (left + right) // 2
        (llstreak, lrstreak, lmaxstreak) = WHATDOIDO(left, m)
        (rlstreak, rrstreak, rmaxstreak) = WHATDOIDO(m+1, right)

        if A[m] == A[m+1]:
            maxstreak = max(lmaxstreak, rmaxstreak, lrstreak+rlstreak)
            if lmaxstreak == m - left + 1:
                lstreak = lmaxstreak + rlstreak
            else:
                lstreak = llstreak
            if rmaxstreak == right - m:
                rstreak = rmaxstreak + lrstreak
            else:
                rstreak = rrstreak
        else:
            maxstreak = max(lmaxstreak, rmaxstreak)
            lstreak = llstreak
            rstreak = rrstreak
        return (lstreak, rstreak, maxstreak)

if __name__ == '__main__':
    print(WHATDOIDO(0,5))