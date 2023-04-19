def solution(N, number):
    answer = 0
    s = [set() for x in range(8)]
    
    if N == number:
        return 1
    
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))
        
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2) #op2가 0인 경우 division error 발생
        if number in s[i]:  #그때그때 확인을 하면 연산이 단순할 수도 있겠지만 이렇게 list를 확인하는 것이 코드가 깔끔함
            answer = i + 1
            break
    else:
        answer = -1
            
    return answer