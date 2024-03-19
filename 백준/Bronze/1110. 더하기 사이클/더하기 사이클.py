n = int(input())

org_n = n
cnt = 0

while True:
    sum_num = (n // 10) + (n % 10)
    new_num = (n % 10) * 10 + (sum_num % 10)

    cnt += 1

    if org_n == new_num:
        break

    n = new_num

print(cnt)