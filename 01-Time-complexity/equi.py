def solution(A):
    # write your code in Python 2.7
    
    R=sum(A)
    L=0
    
    for x in range(len(A)):        
        if x>0:
            L+=A[x-1]
        R-=A[x]
        
        if L==R:
            return x
    return -1