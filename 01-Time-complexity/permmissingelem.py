# https://codility.com/demo/results/trainingTB24D8-RGA/

def solution(A):
    # write your code in Python 2.7
    
    N=len(A)
    PS = (N+1)*(1+N+1)/2
    S=sum(A)
    return PS-S