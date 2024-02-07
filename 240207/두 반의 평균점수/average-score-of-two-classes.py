from functools import reduce

n = int(input())
scores = list(map(int,input().split()))
groups = list(map(int, input().split()))

sum = reduce(lambda acc, group: acc + (scores[group-1]), groups, 0)
print(round(sum/2,2))