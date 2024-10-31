from collections import Counter

def move_points(points, route):
    path = []
    idx = 0
    
    for i in range(len(route) - 1):
        r1, c1 = points[route[i] - 1]
        r2, c2 = points[route[i + 1] - 1]

        while r1 != r2:
            path.append((r1, c1, idx))
            if r1 < r2:
                r1 += 1
            else:
                r1 -= 1
            idx += 1


        while c1 != c2:
            path.append((r1, c1, idx))
            if c1 < c2:
                c1 += 1
            else:
                c1 -= 1
            idx += 1
        
    path.append((r1, c1, idx))
    return path

def solution(points, routes):
    answer = 0

    robot_paths = [] # 로봇이 이동한 길
    for route in routes:
        robot_paths.extend(move_points(points, route))
    
    coll = Counter(robot_paths) # 충돌 횟수
    for i in coll.values():
        if i >= 2:
            answer += 1
    
    return answer