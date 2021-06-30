def solution(A):
    N = len(A)
    if (N > 0):
       positive = []
       negative = []
       ordered = []
       hundert = 100
       suma = 0
       for i in range(0,101):
           positive.append(0)
           negative.append(0)
    
       for i in range(0,N):
           if (A[i] > 0):
              positive[A[i]] += 1
           else:
              negative[(A[i] * -1)] += 1
    
       while(hundert >= 0):
           if(positive[hundert] > 0):
               while(positive[hundert] > 0):
                   ordered.append(hundert)
                   suma += hundert
                   positive[hundert] -= 1
           if(negative[hundert] > 0):
               while(negative[hundert] > 0):
                   ordered.append(hundert)
                   suma += hundert
                   negative[hundert] -= 1
           hundert -= 1

       for i in range (0,N):
           if ((2 * ordered[i]) <= suma):
               suma -= 2 * ordered[i]
           elif ((i == (N-1)) and (abs(2*ordered[i] - suma) < suma)):
               suma -= 2 * ordered[i]
       return(abs(suma))
    else:
       return(0)

A = [1, 5, -2, 5, 2, 3]
print(solution(A))
       
