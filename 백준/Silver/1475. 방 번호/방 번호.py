n = input()
num_counter = [0] * 10
# 6과 9는 서로 대체 가능하다
# 하지만 홀수인 경우에도 하나는 추가가 되어야 하기 때문에 +1
for num in n:
    if num != '9':
        num_counter[int(num)] += 1
    else:
        num_counter[6] += 1
num_counter[6] = (num_counter[6] + 1) // 2

print(max(num_counter))