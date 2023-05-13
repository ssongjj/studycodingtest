def solution(sizes):
    answer = 0
    #구해야 할 것: 모든 명함을 수납할 수 있는 가장 작은 사이즈의 지갑
    
    #x와 y 중에 더 큰 거를 x로 두고 더 작은 거를 y로 둠 (x든 y든 가로가 될 수도 있고 눕히면 세로도 가로가 될 수 있음)
    #x와 y의 최댓값을 구해서 곱함

    answer = max(max(x) for x in sizes) * max(min(x) for x in sizes)
    return answer