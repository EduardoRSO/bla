#só possuem 2 primos como divisores
#de 1 até n
#somando

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    primes = [i for i in range(len(sieve)) if sieve[i]]
    return primes

def solution(n):
    def aux(n):
        p = set()
        for i in primos:
            while n % i == 0:
                p.add(i)
                n /=i
                if len(p) > 2:
                    return False
        if len(p) == 2:
            return True
        return False
    primos = sieve_of_eratosthenes(n)
    c = 0
    for i in range(1,n+1):
        if aux(i):
            c+=1
    print(c)    
    
if __name__ == '__main__':
    n = int(input())
    solution(n)