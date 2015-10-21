# https://codility.com/demo/results/trainingG6RSS6-DGC/

def solution(A):
    # write your code in Python 2.7
    
    N=len(A)
    
    if N==1:
        return A[0]
        
    ms = A[0]
    me = A[0]
    
    for x in A[1:]:
        me=max(me+x,x)
        ms=max(me,ms)
        
    return ms