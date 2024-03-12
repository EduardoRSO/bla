PRECISAO = 1e-9

def is_possible(R, POSTES, LEN):
    ultima_posicao = 0
    if POSTES[0] - ultima_posicao > R:
        return False
    for posicao in POSTES:
        if posicao - ultima_posicao > 2*R:
            return False
        ultima_posicao = posicao
    if LEN - ultima_posicao > R:
        return False
    return True

def solution(N, L, POSTES):
    left = 0
    right = L
    while abs(right - left) >= PRECISAO:
        mid = (left + right) / 2
        if is_possible(mid, POSTES, L):
            right = mid
        else:
            left = mid
    print(left)

def nao_sei(POSTES, N, L):
    maior_distancia = 0
    for i in range(N-1):
        maior_distancia = max(maior_distancia,(POSTES[i+1]-POSTES[i])/2)
    return max([POSTES[0]-0, maior_distancia,L-POSTES[-1]])

if __name__ == '__main__':
    N, L = map(int, input().split())
    POSTES = sorted(list(map(int, input().split())))
    #print(POSTES)
    print(nao_sei(POSTES,N,L))
    #solution(N, L, POSTES)