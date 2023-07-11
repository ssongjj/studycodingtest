def solution(absolutes, signs):
    answer = sum([absolutes[i]*(-1) if not signs[i] else absolutes[i] for i in range(len(absolutes)) ])
    return answer