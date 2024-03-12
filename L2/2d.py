def consegue(N, T, MAQUINAS, T_MEDIO):
    PRODUTOS = 0
    for T_PRODUCAO in MAQUINAS:
        PRODUTOS += T_MEDIO // T_PRODUCAO
        if PRODUTOS >= T:
            return True
    return False

def solution(N, T, MAQUINAS):
    left = 1
    right = min(MAQUINAS) * T
    while left < right:
        mid = (left + right) // 2
        if consegue(N, T, MAQUINAS, mid):
            right = mid
        else:
            left = mid + 1
    print(left)

if __name__ == "__main__":
    N, T = map(int, input().split())
    MAQUINAS = list(map(int, input().split()))
    solution(N,T,MAQUINAS)
