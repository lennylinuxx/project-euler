#sum is a reserved keyword

result = 2

a1 = 1
a2 = 2
a3 = 0

while (True):
    a3 = a1 + a2
    if(a3 > 4000000):
        break
    if(a3%2 == 0):
        result = result + a3
    a1 = a2
    a2 = a3

print(result)