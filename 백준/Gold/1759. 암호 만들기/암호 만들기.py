def combi_password(start):
    #암호가 완성되었다면 바로 print
    if len(selected) == l:
        vowel_cnt = sum(1 for char in selected if char in vowels) #모음의 수
        consonant_cnt = len(selected) - vowel_cnt #자음의 수

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            result.append(''.join(sorted(selected)))
        return


    for i in range(start, len(alph_list)):
        selected.append(alph_list[i])
        combi_password(i+1)
        selected.pop()


l, c = map(int, input().split())
alph_list = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [char for char in alph_list if char not in vowels]
selected = [] #암호로 선택된 알파벳이 저장되는 리스트
result = [] #암호들의 리스트

combi_password(0)

result.sort()
for password in result:
    print(password)
