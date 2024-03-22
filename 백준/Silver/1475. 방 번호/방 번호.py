from collections import Counter

n = input()
num_list = [int(num) for num in n]

num_counter = Counter(num_list)

# 6과 9는 서로 대체 가능하다
# 하지만 홀수인 경우에도 하나는 추가가 되어야 하기 때문에 +1
num_counter[6] = (num_counter[6] + num_counter[9] + 1)//2
num_counter[9] -= num_counter[9]
answer = num_counter.most_common(1)[0][1]

print(answer)