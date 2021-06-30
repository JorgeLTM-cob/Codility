def solution(A):
   N = len(A)
   c = A[0]
   for i in range(1,N):
      c ^= A[i]
   print(c) 


A = [9, 1, 9]
solution(A)
