n = int(input())
s = input()


for i in range(1, n):
    a = s[:i]
    r = s[::-1]
    b = r[:i][::-1]

    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j]:
            cnt += 1

    if cnt == 1:
        print("YES")
        break
else:
    print("NO")
