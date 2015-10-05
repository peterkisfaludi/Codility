# https://codility.com/demo/results/trainingMV4UGX-E22/

def solution(A):
    # write your code in Python 2.7
    
    A.sort()
    N=len(A)
    
    if N<3:
        return 0
    
    for x in range(N-2):
        p=A[x]
        q=A[x+1]
        r=A[x+2]
        
        if p+q>r and q+r>p and r+p>q:
            return 1
            
    return 0