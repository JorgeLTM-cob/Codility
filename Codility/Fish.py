def solution(A,B):
    N = len(A)
    eaten = 0
    for i in range(0,N):
        if (B[i] == 1):
            if (A[i] > 0):
                A[i] *= -1
            else:
                A[i] = float(-0.5)

    j = N - 1
    while(j >= 0):
        while ((A[j] < 0) and (j + 1) == len(A) and (j > 0)) :
            A.pop(j)
            j -= 1

        if ((A[j] < 0) and (len(A) > 1)):
            current = A[j] * A[j + 1]
            if (current <= 0):
              eaten += 1
              if (A[j+1] > abs(A[j])):
                 A.pop(j)
                 j -= 1
              else:
                 A.pop(j + 1)
        else:
            j -= 1

    return(N - eaten)


A = [0, 3, 1, 2, 5]
B = [1, 1, 1, 1, 0]
print(solution(A,B))
