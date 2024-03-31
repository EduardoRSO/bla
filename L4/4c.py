#dado um fatoiral N, o numero de O é dado pela qtd de 2*5 presentes...
#https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

def solution(n):
    def aux(n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

    c = []
    i = 1
    while True:
        z = aux(i)
        #print(i,z)
        if z == n:
            c.append(i)
            i+=1
        elif z < n:
            i+=1
        else:
            break
    
    k = len(c)
    if k != 0:
        print(k)
        for i in c[:-1]:
            print(i, end = ' ')
        print(c[-1])
    else:
        print(k)        


if __name__ == '__main__':
    n = int(input())
    solution(n)