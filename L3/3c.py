def _solution(n,colors):
    print(n,colors)
    exit()
    color_count = set()
    left = right = i = 0
    min_segment = float('inf')
    while i < n:
        print(f'[{color_count}], {left}, {right}, {min_segment}') 
        if colors[i] not in color_count:
            color_count.add(colors[i])
            i+=1
        else:
            left = right = i
            while i < n and colors[i] in color_count:
                print(f'[{color_count}], {left}, {right}, {min_segment}') 
                i+=1
                right+=1
            min_segment = min(min_segment, right+left)
            while left < right:
                print(f'[{color_count}], {left}, {right}, {min_segment}') 
                color_count.remove(colors[left])
                left+=1
            if i < n:
                color_count.add(colors[i])
            print(f'[{color_count}], {left}, {right}, {min_segment}')          
    print(min_segment)

def solution(n,colors):
    p = 0 #quantidade de cores com mais de uma bandeira fora do segmento
    q = {} #quantidade de bandeiras para um dada cor c fora do segmento
    m = n #tamanho do menor segmento
    l = 0 #left pointer
    r = -1 #right pointer 
    for c in colors:
        q[c] = q.get(c,0)+1
        if q[c] > 1:
            p+=1
    if p == 0:
        m = 0 #não há repetição, então a resposta é 0
    else:
        while True:
            #print(l,r,p,m)
            if 0 < p: #segmento inválido
                if r < n-1:
                    r+=1
                    q[colors[r]] -= 1
                    if q[colors[r]] == 1:
                        p -= 1
                else:
                    break
            if 0 == p: #segmento válido
                m = min(m,r-l+1)
                q[colors[l]]+=1
                if q[colors[l]]>1:
                    p+=1
                l+=1
    print(m)
if __name__ == '__main__':
    n = int(input())
    clr = list(map(int, input().split()))
    solution(n, clr)
