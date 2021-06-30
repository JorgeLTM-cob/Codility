def solution(S):
    N = len(S)
    stack = []
    if (N == 0):
        return (1)

    for i in range(0, N):
       if (S[i] == '('):
           stack.append('(')
       else:
           if (len(stack) > 0):
               stack.pop()
           else:
               return(0)
    
    if (len(stack) == 0):
        return(1)
    else:
        return(0)


S = ""
print(solution(S))
