from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

counter = Counter(n_list)

print(counter[v])
