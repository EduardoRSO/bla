def solution():
    print(sum([int(num) for num in input().split(' ')])) 

def main():
    t = int(input())
    for _ in range(t):
        solution()

main()