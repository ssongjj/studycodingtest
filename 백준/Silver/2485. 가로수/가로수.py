import math

n, *t_list = map(int, open(0).read().split())
t_list.sort()
g = math.gcd(*(y - x for x, y in zip(t_list, t_list[1:])))
result = (t_list[-1] - t_list[0]) // g + 1
print(result - n)