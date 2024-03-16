a, b, v = map(int, input().split())

answer = (v - b)/(a - b)

if answer != int(answer):
    answer = int(answer) + 1
else:
    answer = int(answer)

print(answer)