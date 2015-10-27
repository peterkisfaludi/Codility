# https://codility.com/demo/results/trainingRBR94X-AB9/

def solution(A):
    # write your code in Python 2.7
    N=len(A)
    
    prm=dict.fromkeys(xrange(1,N+1),0)
    cnt=0
    
    for x in A:
        if x <= N and x>=1:
            if prm[x]==0:
                prm[x]=1
                cnt+=1
                if cnt==N:
                    return 1
            else:
                return 0
        else:
            return 0
    return 0