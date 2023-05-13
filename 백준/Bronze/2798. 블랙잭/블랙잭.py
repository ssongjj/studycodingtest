from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))  # n개만큼의 카드 번호를 받는다.

comb_card = list(combinations(card, 3))

result = 0
card_sum = 0
for a, b, c in comb_card:
    card_sum = a + b + c
    
    if card_sum <= m:
        result = max(card_sum, result)

print(result)