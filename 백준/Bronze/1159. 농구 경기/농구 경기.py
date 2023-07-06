num = int(input())

name_list = [input()[0] for _ in range(num)]
answer = []

for i in range(ord('a'), ord('z')+1):
    if name_list.count(chr(i)) >= 5:
        answer.append(chr(i))
if len(answer) == 0:
    print("PREDAJA")
else:
    print(''.join(sorted(answer)))