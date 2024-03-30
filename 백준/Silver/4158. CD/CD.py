import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    sang_cd = [int(sys.stdin.readline().strip()) for _ in range(n)]
    sun_cd = [int(sys.stdin.readline().strip()) for _ in range(m)]

    i = 0
    j = 0
    cnt = 0

    while i < n and j < m:
        if sang_cd[i] == sun_cd[j]:
            cnt += 1
            i += 1
            j += 1
        elif sang_cd[i] > sun_cd[j]:
            j += 1
        else:
            i += 1

    print(cnt)
