def dfs(n, computers, index, explored):
    explored[index] = True
    
    for connect in range(n):
        if connect != index and computers[index][connect] == 1:
            if explored[connect] == False:
                dfs(n, computers, connect, explored)

def solution(n, computers):
    answer = 0
    explored = [ False for i in range(n)]
    # computers의 리스트 각각은 한 컴퓨터의 네트워크임 1이면 연결 0이면 안 연결
    # len(computers) == n 
    for com in range(n):
        if explored[com] == False:
            dfs(n, computers, com, explored)
            answer += 1
    
    return answer