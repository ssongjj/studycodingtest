answer = 0
a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

arr = [[[0] * (len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])


for i in range(len(a)+1):
    for j in range(len(b)+1):
        answer = max(max(arr[i][j]), answer)

print(answer)