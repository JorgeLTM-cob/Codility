def solution(X, Y, D):
    dist = Y - X
    jumps = int(dist / D)
    if ((dist % D) > 0):
        jumps += 1
    print(jumps)

X = 1
Y = 3
D = 1
solution(X, Y, D)
