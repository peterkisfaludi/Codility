# https://codility.com/demo/results/training89TSCH-AEW/

def solution(X, A):
    # write your code in Python 2.7
    N=len(A)
    lvs = dict.fromkeys(xrange(1,X+1),0)
    
    cnt=0
    for i in xrange(N):
        x=A[i]
        if x > N+1:
            continue
        
        if lvs[x]==0:
            lvs[x]=1
            cnt+=1
            if cnt==X:
                return i
    return -1