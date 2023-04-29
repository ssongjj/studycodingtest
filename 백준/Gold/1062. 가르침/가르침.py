import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    words = [0] * n   #각 단어를 비트마스킹을 이용해서 저장할 list

    for i in range(n):
        temp = sys.stdin.readline().rstrip()
        for x in temp:
            words[i] |= (1 << (ord(x) - ord('a')))

    #anta tica: a n t i c  k이 5개보다 작으면 한 글자도 배울 수 없음.
    if k < 5:
        print(0)

    #조합을 이용해서 학습 가능한 모든 경우의 수를 확인
    #antic는 무조건 가지고 있어야 하는 경우의 수이기 때문에 빼고 시작한다
    else:
        essential = ['a', 'c', 't', 'i', 'n']
        others = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

        max_value = 0
        for combi in combinations(others, k-5):
            cnt = 0
            study = 0

            for ch in essential:
                study = study | (1 << (ord(ch) - ord('a')))
            for ch in combi:
                study = study | (1 << (ord(ch) - ord('a')))

            # 필수와 조합의 내용을 모두 학습한 후에
            for word in words:
                if word & study == word: #학습한 게 word와 일치하는지 확인 일치한다면 cnt 1 증가
                    cnt += 1

            max_value = max(max_value, cnt)

        print(max_value)