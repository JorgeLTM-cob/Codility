def solution(A):
    N = len(A)
    if (N == 1):
        return(abs(2*A[0]))
    right = N - 1
    left = 0
    mini = -1
    begin = False
    A.sort()
    while(left < right):
        a = abs(2*A[left])
        b = abs(2*A[right])
        c = abs(A[left] + A[right])
        if (not(begin)):
            mini = min(a,b,c)
            begin = True
        else:
            mini = min(a,b,c,mini)
        if((abs(A[left])) > (abs(A[right]))):
            left += 1
        else:
            right -= 1

    return(mini)

A = [1, 4, -3]
print(solution(A))


        
