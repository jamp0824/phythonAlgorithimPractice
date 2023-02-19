from collections import deque

def solution(maps):
    ROW, COL = len(maps), len(maps[0])
    s_r, s_c = None, None  # 시작 위치
    e_r, e_c = None, None  # 출구 위치
    l_r, l_c = None, None  # 레버 위치
    for i in range(ROW):
        for j in range(COL):
            if maps[i][j] == 'S':
                s_r, s_c = i, j
            elif maps[i][j] == 'E':
                e_r, e_c = i, j
            elif maps[i][j] == 'L':
                l_r, l_c = i, j

    # bfs 탐색
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향
    q = deque([(s_r, s_c, False)])  # (행, 열, 레버를 당겼는지 여부)를 저장하는 큐
    visited = set([(s_r, s_c, False)])  # 방문한 지점을 저장하는 집합
    time = 0  # 경과 시간
    while q:
        for _ in range(len(q)):
            r, c, lever_pulled = q.popleft()
            if r == e_r and c == e_c:  # 출구에 도착한 경우
                return time
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROW or nc < 0 or nc >= COL:
                    continue
                if maps[nr][nc] == 'X':
                    continue
                if (nr, nc, lever_pulled) in visited:
                    continue
                if maps[nr][nc] == 'L' and not lever_pulled:
                    q.append((nr, nc, True))
                    visited.add((nr, nc, True))
                elif maps[nr][nc] == 'O' or maps[nr][nc] == 'E':
                    q.append((nr, nc, lever_pulled))
                    visited.add((nr, nc, lever_pulled))
            time += 1

    return -1  # 탈출할 수 없는 경우

#BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)