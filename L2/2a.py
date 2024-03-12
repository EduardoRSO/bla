def solution(N,X):
    M_i = int(input())
    left = 0
    right = N - 1
    res = 0
    while left <= right:
        mid = (left+right)//2
        if M_i >= X[mid]:
            res = mid +1
            left = mid + 1
        else:
            right = mid -1
    print(res)

if __name__ == '__main__':
    N = int(input())
    X = sorted([int(x_i) for x_i in input().split(' ')])
    Q = int(input())
    for _ in range(Q):
        solution(N,X)
