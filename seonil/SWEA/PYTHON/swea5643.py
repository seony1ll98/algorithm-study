"""
SWEA5643. 키 순서
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())

    # reach[a][b] = True 이면 a < b (a가 b보다 작다)
    reach = [[False] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        reach[a][b] = True

    # 플로이드 워셜: 중간 노드 k를 경유하는 모든 경로 확인
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(N + 1):
                # i -> k -> j 경로가 있으면 i -> j 도 가능
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True
    
    # 각 학생마다 (자기보다 작은 사람 수 + 자기보다 큰 사람 수) == N - 1 이면 순위가 확정된 것임
    answer = 0
    for i in range(1, N + 1):
        smaller = 0
        bigger = 0
        for j in range(1, N + 1):
            if i == j:
                continue
            if reach[j][i]: # j < i
                smaller += 1
            if reach[i][j]: # i < j
                bigger += 1
        
        if smaller + bigger == N - 1:
            answer += 1
    
    print(f'#{tc} {answer}')