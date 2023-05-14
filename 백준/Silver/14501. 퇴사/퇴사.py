n = int(input())
consulting = [tuple(map(int, input().split())) for _ in range(n)]

#그날그날 낼 수 있는 수익 중에 가장 큰 수익을 계산함

cost = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + consulting[i][0] > n:  #consult에 걸리는 기간이 n보다 커지면 이 일은 할 수 없음
        cost[i] = cost[i+1]
    else:
        cost[i] = max(cost[i+1], consulting[i][1] + cost[i + consulting[i][0]])   #i+1번째 날 수익(여태까지 계산한 수익)과 만약 이 cousult를 맡는다면 발생할 수익의 합을 비교하여 더 큰 수익을 고른다

result = cost[0]
print(result)