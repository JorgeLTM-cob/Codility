import math

gap = 0
mayor = 0
num = int(input())
log2 = int(math.log(num,2))
limit1 = 2**log2
log2 += 1
limit2 = 2**log2

if ((limit1 == num) or (limit2 - 1 == num)):
    print("0")
else:
    log2 -= 1
    last = log2    
    while (log2 >= 0):
        a = 2**log2
        if (a <= num):
           num -= a
           gap = last - log2 - 1
           last = log2
           if (gap > mayor):
               mayor = gap
               
        log2 -= 1


    print(mayor)

