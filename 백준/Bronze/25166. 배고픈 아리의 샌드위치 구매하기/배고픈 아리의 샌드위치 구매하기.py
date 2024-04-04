s, m = map(int, input().split())

# << 비트 왼쪽 시프트 연산자
# 모든 수를 1로 설정된 비트마스크를 만들기 위해서 -1
# 1111111111

coin = (1 << 10) - 1
remain = s - coin

if s & ~coin == 0:
    print("No thanks")
elif remain & ~m == 0:
    print("Thanks")
else:
    print("Impossible")
