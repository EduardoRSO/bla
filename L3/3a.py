def solution(n, k, string, l):
    left = 0
    max_length = 0
    count = 0

    for right in range(n):
        if string[right] == l:
            count += 1

        while right - left + 1 - count > k:
            if string[left] == l:
                count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)
    return max_length
    
if __name__ == '__main__':
    n, k = map(int, input().split())
    string = input()
    print(max(solution(n,k,string,'a'),solution(n,k,string,'b')))
    
