
def main():
    t = int(input())
    soma = 0
    for _ in range(t):
        declaracao = input("")
        if declaracao[0] == "+" or declaracao[-1] == "+":
            soma += 1
        else:
            soma -=1
    print(soma) 

main()