import sys
from itertools import combinations

def input_single(dtype=int):
    return dtype(sys.stdin.readline().strip())

def input_list(dtype=int):
    return [dtype(i) for i in sys.stdin.readline().strip().split()]

N, M, H = input_list()
if M == 0:
    print(0)
    exit(0)

L = [[False]*(N+1) for _ in range(H)]
V = [list(range(1, N+1))] + [[0] * N for _ in range(H)]
for _ in range(M):
    i, j = input_list()
    L[i-1][j] = True 
for i in range(1, H+1):
    for j in range(N):
        if L[i-1][j]:
            V[i][j] = V[i-1][j-1]
        elif L[i-1][j+1]:
            V[i][j] = V[i-1][j+1]
        else:
            V[i][j] = V[i-1][j]

W = sum((V[-1][i] == i+1) for i in range(N))
if W == N:
    print(0)
    exit(0)
if W < N-6:
    print(-1)
    exit(0)

E = [(i, j) for i in range(H) for j in range(1, N) if not L[i][j] and not L[i][j-1] and not L[i][j+1]]

def checkLadder(ladders):
    R = list(range(N+1))

    for i, j in ladders:
        n1, n2 = V[i+1][j-1], V[i+1][j]
        R[n1], R[n2] = R[n2], R[n1]

    for n in range(1, 1+N):
        if R[V[-1][n-1]] != n:
            return False

    return True

for ladders in combinations(E, 1):
    if checkLadder(ladders):
        print(1)
        exit(0)

for ladders in combinations(E, 2):
    if ladders[0][0]==ladders[1][0] and abs(ladders[0][1]-ladders[1][1]) == 1:
        continue 
    if checkLadder(ladders):
        print(2)
        exit(0)

for ladders in combinations(E, 3):
    if ladders[0][0]==ladders[1][0] and abs(ladders[0][1]-ladders[1][1]) == 1:
        continue 
    if ladders[0][0]==ladders[2][0] and abs(ladders[0][1]-ladders[2][1]) == 1:
        continue 
    if ladders[1][0]==ladders[2][0] and abs(ladders[1][1]-ladders[2][1]) == 1:
        continue 
    if checkLadder(ladders):
        print(3)
        exit(0)

print(-1)