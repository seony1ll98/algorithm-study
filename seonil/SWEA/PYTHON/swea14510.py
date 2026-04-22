"""
SWEA14510. 나무의 키
"""

def solve(N, trees):
    max_h = max(trees)  # 가장 큰 나무의 키
    diffs = [max_h - h for h in trees]  # 각 나무별로 얼마나 더 자라야 하는지
    total = sum(diffs)  # 모든 나무의 필요 성장량 총합

    # 모든 나무의 필요 성장량이 0이 되면 전부 다 자란 것이므로 종료.
    if total == 0:
        return 0
    
    """
    <핵심 아이디어>
    각 나무의 필요 성장량 d를 (+1을 a번) + (+2를 b번)으로 쪼갬.
    #   → a + 2b = d
    # 짝수 날(+2)을 최대한 많이 쓰면 전체 날짜가 줄어듦.
    """
    sum_half = sum(d // 2 for d in diffs) # 최대 짝수날 사용량
    sum_odd_remain = sum(d % 2 for d in diffs) # 최대 짝수날 사용 이후 남은 홀수 개수

    def feasible(D):
        """
        D일 안에 나무들이 조건을 만족할 수 있는지 판정하는 함수
        """
        odd_days = (D + 1) // 2 # D일 중 홀수 번째 날의 개수
        even_days = D // 2      # D일 중 짝수 번째 날의 개수

        # 짝수 날을 얼마나 쓸 수 있는지 결정하기

        # 짝수 날이 충분히 많아서 원하는 만큼 +2를 쓸 수 있으면
        if even_days >= sum_half:   
            req_odd_days = sum_odd_remain      # 각 나무에서 최소로 필요한 +1 만 쓰면 OK
        
        # 만약 짝수 날이 부족해서 +2를 even_days 밖에 못쓰면 나머지는 전부 +1로 메워야됨
        else:
            req_odd_days = total - 2 * even_days
        
        # 써야 할 +1의 개수가 홀수 날 개수 이하이고, 실제로 물 주는 날의 총합이 D 이하이면 가능
        return req_odd_days <= odd_days and req_odd_days + min(sum_half, even_days) <= D
    
    """
    이분탐색으로 최소 D 찾기
    """
    lo, hi = 1, 2 * total + 5   # 넉넉하게 최악의 경우 2*total에 마진 +5까지 상한으로 잡았음
    while lo < hi:
        # 중간값을 시도
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid        # mid일에 가능하면 범위를 왼쪽으로
        else:
            lo = mid + 1    # mid일에 불가능하면 범위를 오른쪽으로
    
    return lo   # 루프 종료 시 lo == hi == 가능한 최소

# main
T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    trees = list(map(int, input().split()))

    # 정답 출력
    print(f'#{tc} {solve(N, trees)}')