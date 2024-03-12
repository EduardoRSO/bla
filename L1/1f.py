def solution(n):
    for i in range(1, n//3+1):
        for j in range(i+1,(n-i)//2+1):
            k = n - (i+j)
            if i % 3 == 0 or j % 3 == 0 or k % 3 == 0:
                continue
            else:
                if len(set([i,j,k])) == 3:
                    print('YES')
                    print(i,j,k)
                    return
    print('NO')


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solution(int(input()))
