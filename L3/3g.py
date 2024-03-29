def max_days_to_live(n, h, intervals):
    max_days = 0
    total_sunny_days = 0
    left = 0
    for right in range(n):
        total_sunny_days += intervals[right][0] - intervals[right-1][1] if right > 0 and right != left else 0
        while total_sunny_days >= h:
            total_sunny_days -= intervals[left + 1][0] - intervals[left][1]
            left += 1
        current_sum = intervals[right][1] - intervals[left][0] - total_sunny_days
        max_days = max(max_days, current_sum + h)
    print(max_days)

n, h = map(int, input().split())
intervals = [tuple(map(int,input().split())) for _ in range(n)]
max_days_to_live(n, h, intervals)
