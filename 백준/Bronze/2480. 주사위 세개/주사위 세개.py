from collections import Counter

v_list = list(map(int, input().split()))
counter = Counter(v_list)

if len(counter) == 1:
    answer = 10000 + v_list[0] * 1000
elif len(counter) == 2:
    answer = 1000 + counter.most_common(1)[0][0] * 100
else:
    answer = max(v_list) * 100

print(answer)