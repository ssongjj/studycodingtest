def solution(genres, plays):
    # 속한 노래가 많이 재생
    # 장르 내 가장 많이 재생된 노래
    # 장르에서 재생 횟수가 같으면 고유 번호가 낮은 노래 (고유 번호 부여 필요)
    answer = []
    m_dicts = { e: [] for e in set(genres)} # 장르의 중복 제거를 위해
    
    for m in zip(genres, plays, range(len(plays))):
        m_dicts[m[0]].append((m[1], m[2]))
        
    # 최대 장르 선정, play 순으로 선 정렬 (내림차순) 후 고유 번호로 정렬 (오름차순)
    genreSort = sorted(m_dicts.keys(), key = lambda x: sum(map(lambda y: y[0], m_dicts[x])), reverse = True)
    
    for genre in genreSort:
        idx = [ e[1] for e in sorted(m_dicts[genre], key = lambda x: [-x[0], x[1]])]
        answer.extend(idx[:min(len(idx), 2)])
    
    return answer
