import time
start = time.perf_counter()

result = 60

def div_test(n):
    for i in [11,13,14,16,17,18,19]:
        if(n % i != 0):
            return False
    return True
    
while(True):
    if(div_test(result)):
        break
    result += 60
        
print(result)

duration = time.perf_counter() - start
print(duration)

        