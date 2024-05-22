import math

n = int(input())
a = int(input())
result = 0

t_list = []

for i in range(n-1):
    tree = int(input())
    t_list.append(tree - a)
    a = tree

g = math.gcd(*t_list)

# 각 간격에 들어갈 수 있는 가로수의 수 (t // g는 간격 t를 최대 공약수 g로 나눈 몫이기 때문에 해당 간격에 들어갈 수 있는 가로수)
# 1을 빼는 이유는 해당 간격에 들어갈 가로수의 총 수기 때문에 한 개는 이미 존재하는 가로수
for t in t_list:
    result += t // g - 1

print(result)