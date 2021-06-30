def solution(S):
    N = len(S)
    if (N == 0):
        return (1)
    openclose = {}
    openclose['}'] = '{'
    openclose[']'] = '['
    openclose[')'] = '('
    stack = []
    for i in range(0,N):
        if (S[i] in openclose.keys()):
            if (len(stack) > 0):
                if (openclose[S[i]] == stack.pop()):
                   pass
                else:
                   return (0)
            else:
                return(0)
        else:
            stack.append(S[i])
    if (len(stack) == 0):
        return (1)
    else: 
        return (0)

S = ")([)()]"
print(solution(S))
