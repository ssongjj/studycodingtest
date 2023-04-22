#최적의 위치가 될 수 있는 건물 번호 두 개, 그때 모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간의 총합
import sys
from itertools import combinations
from collections import deque

def bfs(node1, node2, visited):
    visited[node1] = True
    visited[node2] = True
    scores = [0 for _ in range(N + 1)]

    while q:
        cur, depth = q.popleft()
        if scores[cur] == 0:  # 아직 방문하지 않았다면 왕복으로 방문해야 함
            scores[cur] = depth * 2
        for next in tree[cur]:
            if not visited[next]:
                visited[next] = True
                q.append([next, depth + 1])
    return [sum(scores), node1, node2]

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    #트리 생성
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    #치킨 집을 임의로 두 개 선택했을 때 각 노드에서 치킨 집까지 거리와 치킨 집을 담을 리스트
    score_list = []
    #임의의 두 개 치킨 집 선택 (조합 이용)
    combi = list(combinations([i for i in range(1, N + 1)], 2))

    for node in combi:
        node1, node2 = node
        q = deque()
        #각 치킨 집 노드부터 탐색 시작
        q.append([node1, 0])
        q.append([node2, 0])
        visited = [False] * (N+1)
        score_list.append(bfs(node1, node2, visited))
    score_list.sort()
    print(f'{score_list[0][1]} {score_list[0][2]} {score_list[0][0]}')
