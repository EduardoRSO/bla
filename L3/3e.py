def _count_balanced_pairs(n, heights):
    total_height = sum(heights)
    target_height = total_height * (n-2)
    count = 0
    heights.sort()  
    left, right = 0, n - 1
    while right > left:
        current_height = (total_height - heights[left] - heights[right])*n 
        #print(left,right,target_height, current_height)
        if current_height == target_height:
            count +=1
        if left == right -1:
            right -= 1
            left = 0
        else:
            left += 1
    return count

def count_balanced_pairs(n, heights):
    total_height = sum(heights)
    target_height = total_height * (n-2)
    count = 0
    left, right = 0, n-1
    while left < right:
        current_height = (total_height - heights[left] - heights[right]) * n
        #print(left,right,target_height, current_height)
        if current_height == target_height:
            count+=1
        if current_height > target_height:
            left+=1
            right=n-1
        else:
            right-=1
            if right <= left:
                left+=1
                right=n-1      
    return count

def solution(n,heights):
    s = sum(heights) #soma das alturas
    c = {} #quantidade de plantas com a altura H
    for h in heights:
        c[h] = c.get(h,0)+1
    u = list(c.keys()) # array ordenado com todas as n alturas
    l = 0 #left pointer
    m = len(u) 
    r = m-1#right pointer
    p = 0 #numero de pares
    target = 2*s
    #print(u,l,r)
    while l < r:
        current_sum = n * (u[l] + u[r])
        #print(current_sum, target)
        #print(u[l],u[r],p)
        if current_sum < target:
            l+=1
        elif target < current_sum:
            r-=1
        else:
            if u[r] != u[l]:
                p += c[u[l]] * c[u[r]]
            else:
                p += c[u[l]] * (c[u[r]]-1)//2
            if r > l+1:
                r-=1
            else:
                r = m-1
                l+=1
            
    if n * (u[l] + u[r]) == target:
        p += c[u[l]] * (c[u[r]]-1)//2
    print(p)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        heights = sorted(list(map(int, input().split()))) 
        solution(n, heights)
