def solution(s):
    answer = ''
    result = []
    words = s.split(' ')  # 공백 기준으로 나누되, 공백을 포함하여 나눔
    
    for word in words:
        if word:  # 단어가 비어있지 않을 때
            if word[0].isalpha():
                result.append(word[0].upper() + word[1:].lower())
            else:
                result.append(word.lower())
        else:  # 단어가 비어있을 때 (공백만 있는 경우)
            result.append('')

    answer = ' '.join(result)
    return answer