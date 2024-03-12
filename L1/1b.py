def solution():
    n = int(input())
    negativos = 0
    temZero = 0
    for elem in [int(a) for a in input().split(' ')]:
        if elem < 0:
            negativos +=1
        elif elem == 0:
            temZero +=1
            break
    if temZero > 0:
        print(0)
    elif negativos % 2 != 0:
        print(0)
    else:
        print(1)
        print(n,0)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solution()
