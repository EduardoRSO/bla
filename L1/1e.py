def solution(t):
    soma = 0
    for n in input().split(' '):
        soma += int(n)
    print(int((t**2+t)/2-soma))

if __name__ == '__main__':
    t = int(input())
    solution(t)
