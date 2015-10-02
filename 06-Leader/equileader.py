https://codility.com/demo/results/trainingZAHTRM-2C9/

from collections import Counter

def solution(A):
    # write your code in Python 2.7
    cnt=0
    N=len(A)
    
    R = dict(zip(set(A),[0]*len(set(A))))
    L = dict(zip(set(A),[0]*len(set(A))))
    
    maxR = None
    cntR = 0

    maxL = None
    cntL = 0
    
    Rarr=[0]*(N-1)
    Larr=[0]*(N-1)
    
    for x in xrange(N-1):
        L[A[x]]+=1
        if L[A[x]]>=cntL:
            maxL = A[x]
            cntL = L[A[x]]
        
        if cntL>(x+1)//2:
            Larr[x]=maxL
        else:
            Larr[x]=None            

    for x in xrange(N-1):
        R[A[N-1-x]]+=1
        if R[A[N-1-x]]>=cntR:
            maxR = A[N-1-x]
            cntR = R[A[N-1-x]]
        
        if cntR>(x+1)//2:
            Rarr[x]=maxR
        else:
            Rarr[x]=None
    
    Rarr=Rarr[::-1]
    
    for x in range(N-1):
        if Larr[x]==None or Rarr[x]==None:
            continue
        if Larr[x]==Rarr[x]:
            cnt+=1
    
    
    return cnt