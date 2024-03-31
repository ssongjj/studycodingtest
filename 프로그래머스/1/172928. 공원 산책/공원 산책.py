op = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}


def move(park, pos, direction, distance):
    new_pos = pos[:]
    dx, dy = op[direction]  # 이동 방향에 따른 변화값 가져오기
    for _ in range(distance):
        nx, ny = new_pos[0] + dx, new_pos[1] + dy  # 새로운 위치 계산

        if not (0 <= nx < len(park) and 0 <= ny < len(park[0])) or park[nx][ny] == "X":
            return pos
        new_pos = [nx, ny]

    return new_pos


def find_start(park_map):
    for i in range(len(park_map)):
        if "S" in park_map[i]:
            j = park_map[i].index("S")
            return [i, j]


def solution(park, routes):
    park_map = [list(p) for p in park]
    pos = find_start(park_map)

    for route in routes:
        direction, distance = route.split(" ")
        pos = move(park_map, pos, direction, int(distance))

    return pos
