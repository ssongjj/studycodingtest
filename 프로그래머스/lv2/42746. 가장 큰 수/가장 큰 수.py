import heapq

def solution(numbers):

    answer = ''
    numbers.sort(reverse=True, key = lambda x : str(x)*3)
    
    if numbers[0] == 0:
        return "0"
    
    answer = ''.join(list(str(x) for x in numbers))
    '''

    num_lst = [ str(n) for n in numbers ]
    heapq.heapify(num_lst)
    n = heapq.nlargest(len(num_lst), num_lst)
    
    answer = ''.join(n)
    '''
    
    return answer