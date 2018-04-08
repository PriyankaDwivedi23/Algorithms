def min(a):
    n = len(a)
    S =[0 for x in range(n)]
    for j in range(1,len(a)):
        S[j] = 99999
        for k in range(1,j+1):

            if a[k] == a[j] and S[j]>S[k-1]+1:
                S[j] = S[k-1]+1
    return S

if __name__ == '__main__':
    a =[8,2,6,7,1,2,3,4,5,4,5,3,1]
    print(min(a))
