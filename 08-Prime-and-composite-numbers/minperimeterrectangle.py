https://codility.com/demo/results/trainingBSB6MB-WKQ/

from math import sqrt
def solution(N):
    # write your code in Python 2.7
    
    chk=int(sqrt(N))
    mn=2*(1+N)
            
    for x in range(1,chk+1):
        a=x
        b=N//x
        if a*b==N:
            mn=min(mn,2*(a+b))
    return mn