def solution(s):
    n = len(s)
    transitions = [0]*n
    for i in range(1,n):
        transitions[i] = 0
        if s[i] == s[i - 1]:
            transitions[i] = transitions[i - 1] + 1
        else:
            transitions[i] = transitions[i - 1]
    return transitions


if __name__ == '__main__':
    s = input().strip()
    m = int(input())
    transitions = solution(s)
    for _ in range(m):
        li, ri = map(int, input().split())
        print(transitions[ri-1] - transitions[li-1])
