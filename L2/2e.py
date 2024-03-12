def conta(ESTABULOS, d):
    vacas = 1
    ultimo = ESTABULOS[0]
    for estabulo in ESTABULOS:
        if estabulo - ultimo >= d:
            vacas += 1
            ultimo = estabulo
    return vacas

def solution(ESTABULOS, C):
    left = 0
    right = ESTABULOS[-1] - ESTABULOS[0]
    while left <= right:
        mid = (left + right) // 2
        if conta(ESTABULOS, mid) >= C:
            left = mid + 1
        else:
            right = mid - 1
    print(right)

if __name__ == "__main__":
    for _ in range(int(input())):
        N, C = map(int, input().split())
        ESTABULOS = sorted([int(input()) for _ in range(N)])
        solution(ESTABULOS, C)
