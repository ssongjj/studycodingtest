res = []

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        sang_cd = [int(input()) for _ in range(n)]
        sun_cd = [int(input()) for _ in range(m)]

        sang = set(sang_cd)
        sun = set(sun_cd)

        res.append(str(len(sang & sun)))

print("\n".join(res))
