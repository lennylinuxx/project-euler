import time
start = time.perf_counter()

import math

def is_prime(n):
    for i in range(3,int(math.sqrt(n))+1,2): #testing only odd nos.
        if(n%i == 0):
            return False
    return True

total = 0

for x in range(3,2000000,2):
    if(is_prime(x)):
        total += x

print(total+2)
        

duration = time.perf_counter() - start
print(duration)

        