def solution(H):

   N = len(H)
   blocks = 1
   stack = []
   stack.append(0)
   stack.append(H[0])
   sindex = 1
   for i in range (1,N):
       if (H[i] > stack[sindex]):
           stack.append(H[i])
           sindex += 1
           blocks += 1
       elif (H[i] < stack[sindex]):
           while((stack[sindex] > H[i]) and (sindex > 0)):
               stack.pop()
               if (sindex > 0):
                  sindex -= 1
           if ((len(stack) == 1) or (stack[sindex] < H[i])):
               stack.append(H[i])
               sindex += 1
               blocks += 1

   return(blocks)


H = [1, 20, 1]
print (solution(H))

