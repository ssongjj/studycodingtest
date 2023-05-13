n, m = map(int, input().split())
card = sorted(list(map(int, input().split())), reverse=True)  # n개만큼의 카드 번호를 받는다.

result = 0
for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      card_sum = card[i]+card[j]+card[k]
      if card_sum <= m:
        if result < card_sum:
            result = card_sum
        break

print(result)