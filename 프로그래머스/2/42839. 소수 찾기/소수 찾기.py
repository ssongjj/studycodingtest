from itertools import permutations 

def find_sosu(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = []
    p_list = []
    n_list = []
    num_lst = list(int(num) for num in numbers)
    
    for i in range(1, len(num_lst)+1):
        p_list.extend(permutations(num_lst, i))
    
    for num in p_list:
        n_list.append(int(''.join(list(str(n) for n in num))))
    
    for num in set(n_list):
        if find_sosu(num):
            answer.append(num)

    return len(answer)
'''
def find_sosu(num): #소수를 판별하는 함수
    if num < 2:
        return False
    
    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = []
    p_list = [] #문자열을 분리해서 나오는 모든 경우의 순열 리스트
    
    for i in range(1, len(numbers)+1):
        p_list.extend(permutations(numbers, i)) 
        
    for n_list in p_list:
        num  = int(''.join([str(n) for n in n_list]))
        if find_sosu(num):
            answer.append(num)
    
    return len(set(answer))
'''

'''
#에라토스테네스의 체
def solution(numbers):
    answer = 0
    a = set()
    
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i+1))))
        #조합들의 리스트를 str으로 형변환해 주고 이후 정수로 형변환 해 준 후 set을 통해 중복 제거 후 |= update(a를)
    
    a -= set(range(0, 2)) #2보다 작은 수는 소수가 아님
    
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    
    answer = len(a)
    
    return answer
'''