
# 오븐을 위에서부터 아래로 확인하는데
# 만약 현재 관의 지름이 이전 관의 지름보다 크더라도 이전 관의 지름만큼의 반죽만 들어감

d, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))

# 현재 관 > 이전 관 = 이전
# 이진탐색은 정렬된 리스트여야 한다
for i in range(1, len(oven)):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

#이걸 어떻게 이분 탐색으로 풀 수 있을까?
#어느 부분에 쌓였는지 위치를 check
#다만 배열이 내림차순이라는 것을 인식하자
#이때 최솟값과 최댓값의 설정을 oven의 index로 사용하기 위해 oven 길이 - 1까지로 한다.
left, right = 0, len(oven)-1
location = 0
for dough in doughs:
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if oven[mid] >= dough: #도우를 더 쌓을 수 있다는 뜻으로 left 값 조정 필요
            left = mid + 1
            location = mid
            flag = True
        else:
            right = mid - 1

    if not flag:
        location = -1
        break

    left = 0
    right = location - 1

if location  == -1:
    print(0)
else:
    print(location + 1)