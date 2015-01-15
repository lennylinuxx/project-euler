res_array = []

for i in range(1000):
    if(i%3 == 0):
        res_array.append(i)
        
for i in range(1000):
    if(i%5 == 0 and (i not in res_array)):
        res_array.append(i)
        
print(sum(res_array))