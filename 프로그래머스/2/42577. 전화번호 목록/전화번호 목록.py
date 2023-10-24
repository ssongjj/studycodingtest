def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i, num in enumerate(phone_book):
        if i != 0:
            if num.startswith(phone_book[i-1]):
                return False
            
    return answer
        
        