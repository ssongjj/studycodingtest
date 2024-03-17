n = int(input())

card = [x for x in range(n, 0, -1)]
answer = []

while card:
    answer.append(card.pop())
    if len(card) != 0:
        card.insert(0, card.pop())

print(*answer)