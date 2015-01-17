import time
start = time.perf_counter()

sum_of_squares = 0


for i in range(1,101):
    sum_of_squares += i**2

square_of_sum = (50*101)*(50*101)

print(square_of_sum - sum_of_squares)


duration = time.perf_counter() - start
print(duration)
