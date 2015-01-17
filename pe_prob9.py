import time
start = time.perf_counter()

x = 0
y = 0
z = 0

for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 - (a+b)
        if(c**2 == (a**2) + (b**2)):
            x = a
            y = b
            z = c
            break

print(x*y*z)
        

duration = time.perf_counter() - start
print(duration)