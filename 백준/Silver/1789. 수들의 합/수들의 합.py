s = int(input())

#합쳐지는 자연수의 개수가 많아지려면 결국 제일 작은 수들의 합으로 해당 수를 만들어야 됨  
for i in range(1, s+1):
    if s - i < 0: #차가 음수가 되면 종료
        break
    s -= i
    result = i
    
print(result)