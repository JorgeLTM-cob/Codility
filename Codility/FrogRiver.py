def solution(X, A):
    N = len(A)
    expected = int((X * (X + 1))/2)
    suma = 0
    Leaves = []
    for i in range(0,(X+1)):
        Leaves.append(False)
    for i in range(0,N):
        if (not(Leaves[A[i]])):
            Leaves[A[i]] = True
            suma += A[i]
            if (suma == expected):
                return(i)
                break
    return(-1)


A = [4]
X = 5
print(solution(X, A))
