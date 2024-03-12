def consegue(K,X,p):
    X = sorted(X,key=lambda x: x[0]+ x[1] * p)
    t = [0,0]
    C = 0
    for i in range(p):
        t[0] += X[i][0]
        t[1] += X[i][1]
        C = t[0] + t[1]*p
        if C > K:
            return False, C, X
    return True, C, X


def solution(N,K,X):
    left = 0
    right = N -1
    C = 0
    #print(X)
    while left <= right:
        mid = (left + right) // 2
        res, tmp, X = consegue(K,X,mid+1) 
        #print(X,mid)
        if res:
            C = tmp
            left = mid +1
        else:
            right = mid -1
    print(left,C)        

if __name__ == '__main__':
    N, K = [int(x) for x in input().split(' ')]
    #X = sorted([[int(custo_base), (index+1)] for index, custo_base in enumerate(input().split())],key=lambda x: x[0]+ x[1])
    X = [[int(custo_base), (index+1)] for index, custo_base in enumerate(input().split())]
    solution(N,K,X)
    