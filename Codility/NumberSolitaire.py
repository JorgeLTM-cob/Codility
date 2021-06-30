def solution(A):
    N = len(A)
    suma = 0
    suma += A[0]
    suma += A[N - 1]
    for i in range(1, N - 1):
        if (A[i] > 0):
            suma += A[i]
    return(suma)

A = [1, -2, 0, 9, -1, -2]
print(solution(A))
    
