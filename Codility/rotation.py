
A = []
K = 9
arr = []
N = len(A)
if ( N > 0 ):
   if (K > 0):
      real = N - (K % N)
   else:
      real = 0 
   pos = 0
   for j in range(0,N):
      if (real < N):
         arr.append(A[real])
         real += 1
      else:
         arr.append(A[pos])
         pos += 1

print(arr)


