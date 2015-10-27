# https://codility.com/demo/results/training9YF5C7-A7M/

def solution(A):
    # write your code in Python 2.7
    N=len(A)
    ints = dict.fromkeys(xrange(1,N+1),0)
    
    for x in A:
        if x>=1 and x<=N:
            ints[x]=1
            
    for k,v in ints.iteritems():
        if v==0:
            return k
    return N+1