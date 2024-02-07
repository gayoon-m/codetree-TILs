n = int(input())
numbers = list(map(int, input().split(' ')))
sum = 0
count = 0

for i in range(1, n):
    if i % 2 ==0:
        sum += numbers[i-1]
        count+=1

print(f'{sum} {round(sum/count,2)}')