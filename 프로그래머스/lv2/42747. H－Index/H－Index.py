def solution(citations):
    # H-index n편 중 h번 이상 인용 논문 h편 이상 / 나머지 논문이 h번 이하 인용 => h의 최댓값
    # 발표한 논문의 수와 인용된 논문의 수가 같을 때 H-index 개념 참고
    citations.sort()
    for i, citation in enumerate(citations):
        if citation >= len(citations)-i:
            return len(citations)-i

    return 0
