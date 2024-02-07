from functools import reduce

n = int(input())
numbers = list(map(int, input().split(' ')))

even_sum = 0
for i in range(1, n, 2):  
    even_sum += numbers[i]

even_avg = even_sum / (n // 2)  

print(even_sum, format(even_avg, ".1f"))