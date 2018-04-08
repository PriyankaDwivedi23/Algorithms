def Max(A):
    n = len(A)
    if n < 2:
        return A
    else:
        k = (n+1)//2
        B = A[0:k]
        C=A[k+1:]
        mB =Max(B)
        mC = Max(C)
        return max(mB,mC)


def Max1(A,l,r):
    n = len(A)
    if l == r:
        return A[l]
    else:
        k = (l+r)//2

        mB =Max1(A,l,k)
        mC = Max1(A,k+1,r)
        return max(mB,mC)


if __name__ == '__main__':

    # n = [int(x) for x in input().split(" ")]
    n =[2, 4, 6, 10, 1, 4, 3]
    print(Max1(n,0,len(n)-1))