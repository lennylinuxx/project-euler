import time
start = time.perf_counter()

largest = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        prod = x * y
        prodstr = str(prod)
        revprod = int(prodstr[::-1])
        if(prod == revprod):
            if(prod > largest):
                largest = prod

print (largest)

duration = time.perf_counter() - start
print(duration)
