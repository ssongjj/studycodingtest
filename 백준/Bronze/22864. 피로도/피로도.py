a, b, c, m = map(int, input().split())
work = 0
fatigue = 0

for _ in range(24):
    # 일하는 경우
    if fatigue + a <= m:
        work += b
        fatigue += a
    # 쉬는 경우
    else:
        fatigue = max(fatigue - c, 0)

print(work)
