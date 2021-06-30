def solution(A):
    N = len(A)
    expected = ((N + 1)*(N + 2)) / 2
    got = 0
    for i in range(0,N):
       got += A[i]
    miss = int(expected) - got
    return(miss)

A = []
print(solution(A))
