from collections import Counter

n, m = map(int, input().split())
dnas = [input() for _ in range(n)]

result = ""
hamming_code = 0
for i in range(m):
    dna_counts = Counter(s[i] if m > i else "" for s in dnas)
    max_count = max(dna_counts.values())
    max_char = sorted(c for c, count in dna_counts.items() if count == max_count) #아예 가장 많이 나온 문자를 구할 때 sort를 해 준다
    result += max_char[0]  # 문자열의 가장 앞에 추가

for dna in dnas:
    hamming_code += sum(c1 != c2 for c1, c2 in zip(dna, result))  #각각의 문자 위치별로 비교해서 둘이 다른 경우 True를 반환하도록 함 True는 1이므로 sum 함수를 써서 합산 시 1이 더해짐

print(result)
print(hamming_code)