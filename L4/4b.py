#Maximum possible GCD for a pair of integers with sum N
#https://www.geeksforgeeks.org/maximum-possible-gcd-for-a-pair-of-integers-with-sum-n/

def solution(n):
    a = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            a = n//i
            break
        i+=1
    print(a,n-a)
t = int(input())
for _ in range(t):
    n=int(input())
    solution(n)