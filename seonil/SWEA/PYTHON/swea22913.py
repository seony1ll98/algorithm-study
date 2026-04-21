"""
22913. 사과 먹기 게임 1
"""

def count_turns(cy, cx, d, ty, tx):
    """
    현재 (cy, cx)에서 방향 d로 출발해 (ty, tx)에 도달하는 최소 우회전 수
    """
    ddy, ddx = ty - cy, tx - cx # 현재 위치에서 목적지까지의 벡터

    # 좌표 정규화: 어느 방향이든 "오른쪽 보는 시점"으로 변환해서 생각하기
    for _ in range(d):
        ddy, ddx = -ddx, ddy

    # 만약 목적지 벡터가 오른쪽이라면 그대로 오른쪽 방향으로 가면 됨
    if ddy == 0 and ddx > 0:
        return 0
    # 우하단이라면, 1회 우회전 필요
    elif ddy > 0 and ddx > 0:
        return 1
    # 좌하단 또는 정아래이라면, 2회 우회전 필요
    elif ddy > 0 and ddx <= 0:
        return 2
    # 위쪽 영역이라면, 3회 회전 필요
    else:
        return 3

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 사과 찾기
    apples = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                apples.append((arr[i][j], i, j))

    apples.sort() # 사과를 순서 오름차순으로 정렬

    # 시작 지점에서 오른쪽 방향으로 출발
    cy, cx, cd = 0, 0, 0
    total_turns = 0

    # 각 사과 지점 좌표까지의 최소 회전 수 계산
    for _, ty, tx in apples:
        turns = count_turns(cy, cx, cd, ty, tx) # 목적지까지 필요한 최소 우회전 수 계산
        total_turns += turns                    # 회전 수 누적
        cd = (cd + turns) % 4                   # 도착 시 방향 갱신
        cy, cx = ty, tx                         # 목적지 좌표로 현재 좌표 갱신
    
    # 결과 반환
    print(f'#{tc} {total_turns}')
