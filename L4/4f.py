#https://www.geeksforgeeks.org/series-largest-gcd-sum-equals-n/
import math

def solution(n,m):
    def aux(x):
        return bin(x).count('1')

    n %= m 
    if n == 0:
        return 0
    a = n // math.gcd(n,m)
    b = m // math.gcd(n,m)
    #print(a,b)
    if aux(b)>1:
        return -1
    
    return aux(a)*m-n

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(solution(n,m))