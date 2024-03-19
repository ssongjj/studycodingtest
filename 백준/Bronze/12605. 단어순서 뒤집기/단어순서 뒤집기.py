n = int(input())
answer = []

for _ in range(n):
    word_list = list(input().split())
    reversed_word = ' '.join(word_list[::-1])
    answer.append(reversed_word)

for i, word in enumerate(answer):
    print("Case #" + str(i+1) + ": " + word)