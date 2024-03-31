def solution(a, n, k) : 
    s = set(); 
    for i in range(n) :
        if ((a[i] % k == 0 and a[i] // k not in s ) or a[i] % k != 0) :
            s.add(a[i])
    return len(s)

n,k = map(int,input().split())
l = sorted(map(int,input().split()))
print(solution(l,n,k))