https://codility.com/demo/results/trainingVSFHEE-ZHX/

def solution(A, B):
    # write your code in Python 2.7
    
    N=len(A)
    
    if N<2:
        return N
        
    cnt=0
    b=-1
    for x in range(N):
        if A[x]>b:
            cnt+=1
            b=B[x]
            
    return cnt