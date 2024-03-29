if __name__ == '__main__':
    n, q = map(int, input().split())  
    heroes = sorted(list(map(int, input().split())),reverse=True)
    rounds = []
    r = 0
    soma = 0
    for _ in range(q):
        a,b = list(map(int, input().split()))
        rounds.append([a,b])
        r = max(r,b)    
    e = [0]*(r+2)
    s = [0]*(r+2)
    for i in rounds:
        e[i[0]] +=1
        e[i[1]+1] -=1

    for i in range(r+2):
        #print(i, soma, e[i])
        soma += e[i]
        s[i] = soma
    s = sorted(s,reverse=True)
    #print(rounds,e, s)
    #exit()
    total_damage = sum([heroes[i]*s[i] for i in range(n)])
    print(total_damage)

