def solution(A, B):
    N = len(A)
    nonov = 1
    if (N == 0):
        return (0)

    ref = B[0]
    for i in range(1,N):
        if(not(A[i] <= ref)):
               nonov += 1
            ref = B[i]
    return(nonov)

A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]
print(solution(A,B))

