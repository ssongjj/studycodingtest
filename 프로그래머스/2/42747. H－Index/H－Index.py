def solution(citations):
    # H-index n편 중 h번 이상 인용 논문 h편 이상 / 나머지 논문이 h번 이하 인용 => h의 최댓값
    # 발표한 논문의 수와 인용된 논문의 수가 같을 때
    citations.sort()
    for idx, c in enumerate(citations):
        if c >= len(citations) - idx:
            return len(citations) - idx
            
    return 0