import math

def get_divisors(n,max_gcd):
    d = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i <= max_gcd:
                if i > d:
                    d = i
                if n // i <= max_gcd:
                    if n // i > d:
                        d = n // i
            else:
                break
    return d


def solution(x,n):
    max_gcd = x//n
    if max_gcd == 1:
        return 1
    return get_divisors(x,max_gcd)



t = int(input())
for _ in range(t):
    x,n = map(int,input().split())
    print(solution(x,n))