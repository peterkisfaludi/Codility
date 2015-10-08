# https://codility.com/demo/results/training267EB3-K8M/

from math import sqrt
def solution(N):
    # write your code in Python 2.7
    
    cf=0
        
    for x in range(1,int(sqrt(N))+1):
        
        if N%x==0:
            d=N//x
            if d!=x:
                cf+=2
            else:
                cf+=1
                
    return cf