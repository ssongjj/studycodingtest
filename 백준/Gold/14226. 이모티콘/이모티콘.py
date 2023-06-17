from collections import deque

def bfs(target):
    queue = deque()
    queue.append((1, 0)) #영선이가 초기화면에 이미 이모티콘 하나를 입력함 (화면에 입력된 이모티콘, 클립보드 이모티콘)

    visited = set()
    visited.add((1, 0))

    time = 0

    while queue:
        for _ in range(len(queue)):
            screen, clipboard = queue.popleft()

            if screen == target:
                return time

            #복사
            if (screen, screen) not in visited:
                queue.append((screen, screen))
                visited.add((screen, screen))

            #붙여 넣기
            if (screen + clipboard, clipboard) not in visited and clipboard != 0: #clipboard(클립보드에 있는 이모티콘)이 존재해야 삭제 가능
                queue.append((screen + clipboard, clipboard))
                visited.add((screen + clipboard, clipboard))

            #삭제
            if (screen - 1, clipboard) not in visited and screen > 0: #screen(화면에 있는 이모티콘)이 0 이상이어야 삭제 가능
                queue.append((screen - 1, clipboard))
                visited.add((screen - 1, clipboard))

        time += 1

    return -1


s = int(input())
answer = bfs(s)
print(answer)
