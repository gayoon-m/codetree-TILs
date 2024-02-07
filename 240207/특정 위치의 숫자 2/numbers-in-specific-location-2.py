from functools import reduce

n = int(input())
numbers = list(map(int, input().split(' ')))

even_sum = sum(numbers[1::2])

print(even_sum, format(even_sum / (n // 2), ".1f"))