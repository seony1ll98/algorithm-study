"""
BOJ2110. 공유기 설치

[문제]
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

[입력]
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

[출력]
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

# 상하좌우 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 탐색 함수: 시작 좌표에서 연결된 1들의 넓이를 구함
def check_picture(start):
    global cnt_pictures  # 전체 그림 수를 세는 전역 변수
    sy, sx = start

    # 시작점이 0이면 그림이 아님
    if paper[sy][sx] == 0:
        return 0
    else:
        q = deque([start])  # BFS를 위한 큐
        visited[sy][sx] = True  # 시작점 방문 체크
        cnt_pictures += 1  # 그림 개수 하나 추가
        cnt_area = 1  # 현재 그림 넓이 1로 시작

        # BFS 시작
        while q:
            y, x = q.popleft()
            for dir in range(4):  # 상하좌우 네 방향 탐색
                ny, nx = y + dy[dir], x + dx[dir]
                # 다음 좌표가 범위 내에 있고, 아직 방문하지 않았으며, 값이 1인 경우,
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and paper[ny][nx] == 1:
                    q.append((ny, nx))  # 큐에 다음 좌표 enqueue
                    cnt_area += 1   # 넓이 1칸 늘리기
                    visited[ny][nx] = True  # 다음 좌표 방문 체크

    return cnt_area  # BFS 탐색 완료 후 현재 그림의 넓이 반환

# main
n, m = map(int, input().split())    # n: 행 개수, m: 열 개수
paper = [list(map(int, input().split())) for _ in range(n)] # 도화지 입력 받기
visited = [[False] * m for _ in range(n)]   # 방문 여부 저장 배열

cnt_pictures = 0  # 전체 그림 수
max_area = 0      # 가장 큰 그림 넓이

# 모든 도화지 셀에 대해 탐색
for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # 아직 방문하지 않았다면
            area = check_picture((i, j))  # BFS로 그림의 넓이 구함
            max_area = max(area, max_area)  # 최대 넓이 갱신

# 출력: 그림 수, 가장 큰 그림의 넓이
print(cnt_pictures)
print(max_area)
