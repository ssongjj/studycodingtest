def solution(s, n):
    answer = ''
    for ch in s:
        add_ascii = ord(ch) + n
        
        if ord(ch) <= ord("Z") and add_ascii > ord("Z"):
            add_ascii = ord("A") + (add_ascii - ord("Z")) - 1
        elif ord(ch) <= ord("z") and add_ascii > ord("z"):
            add_ascii = ord("a") + (add_ascii - ord("z")) - 1
        
        if ch == " ":
            add_ch = " "
        else:
            add_ch = chr(add_ascii)
            
        answer += add_ch
    return answer