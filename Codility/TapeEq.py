def solution(A):
    menor = 999999
    N = len(A)
    B = []
    B.append(A[0])
    right = N - 1
    for i in range(1,right):
        B.append((B[i-1] + A[i]))
    B.append(A[right])
    right -= 1
    for i in range(0, (N-1)):
        dif = B[right] - B[right + 1]
        if (dif < 0):
            dif *= -1
        B[right] = B[right] - B[right - 1] + B[right + 1]
        right -= 1
        if (dif < menor):
            menor = dif
    return(menor)


A = [1,-1,1]
print(solution(A))
