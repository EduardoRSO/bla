def conta(N, M, MID):
    C = 0
    for i in range(1, N + 1):
        C += min(M, MID // i)
    return C

def solution(N, M, K):
    left = 1
    right = N * M
    while left < right:
        mid = (left + right) // 2
        if conta(N, M, mid) < K:
            left = mid + 1
        else:
            right = mid
    print(left)

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    solution(N, M, K)

