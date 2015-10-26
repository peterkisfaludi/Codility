# https://codility.com/demo/results/trainingXG9VG4-4WN/

def solution(A):
    # write your code in Python 2.7
    
    N=len(A)
    
    L = A[0]
    R = sum(A[1:])
    df=abs(L-R)
    for x in A[1:-1]:
        L+=x
        R-=x
        df=min(df,abs(L-R))
        
    return df