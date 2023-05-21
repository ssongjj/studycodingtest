from itertools import permutations

n = int(input())
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  #1부터 9까지의 수 중에 세 개의 순열을 사용한다 (순서가 매우 중요하다. 그래서 순열을 사용.)

for _ in range(n):
    answer, s, b = map(int, input().split())
    answer = list(str(answer))
    rm_cnt = 0

    for i in range(len(num)):
        s_cnt = b_cnt = 0  #s_cnt 스트라이크 b_cnt는 볼
        i -= rm_cnt

        for j in range(3):
            answer[j] = int(answer[j])
            if answer[j] in num[i]:
                if j == num[i].index(answer[j]):  #자리 수가 일치한다면 스트라이크
                    s_cnt += 1
                else: #그렇지 않다면 볼
                    b_cnt += 1

        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            rm_cnt += 1

print(len(num))