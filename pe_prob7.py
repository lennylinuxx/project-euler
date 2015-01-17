import time
start = time.perf_counter()

import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i == 0):
            return False
    return True

ctr = 0
number = 2

while(True):
    if(ctr == 10001):
        break
    if(is_prime(number)):
        ctr += 1
    number += 1

print(number-1)
    

duration = time.perf_counter() - start
print(duration)

        