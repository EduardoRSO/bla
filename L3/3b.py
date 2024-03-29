def solution(string):
 
    count = [0, 0, 0]
    cnt = 0
    min_days = float('inf')
    left = 0

    for right in range(len(string)):
        dessert = int(string[right]) - 1
        if count[dessert] == 0:
            cnt += 1
        count[dessert] += 1

        while cnt == 3:
            min_days = min(min_days, right - left + 1)
            dessert = int(string[left]) - 1
            count[dessert] -= 1
            if count[dessert] == 0:
                cnt -= 1
            left += 1

    print(min_days if min_days != float('inf') else 0)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solution(input())
