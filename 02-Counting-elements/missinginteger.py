# https://codility.com/demo/results/trainingAGSNEC-76K/

def solution(A):
    # write your code in Python 2.7
    
    A=set(A)
    N=len(A)
    
    d=dict(zip(range(1,N+1),[0]*N))
    
    for x in A:
        d[x]=1
        
    for k,v in d.iteritems():
        if v==0:
            return k
            
    return N+1