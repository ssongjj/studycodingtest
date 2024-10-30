def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)
    
    n, m = len(park), len(park[0]) 
    dp = [[0] * m for _ in range(n)]
    max_len = 0 # 만들 수 있는 최대 사각형의 길이
    
    for i in range(n):
        for j in range(m):
            if park[i][j] == '-1': # 돗자리를 둘 수 있는 공간
                if i == 0 or j == 0: # 시작점 
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_len = max(max_len, dp[i][j])

    for mat in mats:
        if mat <= max_len:
            return mat
                
    return answer