def solution(K,A):

    N = len(A)
    leng = 0
    ropes = 0
    for i in range(0,N):
        leng += A[i]
        if (leng >= K):
            ropes += 1
            leng = 0

    return(ropes)

A = [1, 2, 3, 4, 1, 1, 3]
K = 4
print(solution(K,A))
