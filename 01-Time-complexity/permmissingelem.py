# https://codility.com/demo/results/trainingTF75FS-HZG/

def solution(A):
    # write your code in Python 2.7
    
    N=len(A)
    sm=sum(A)
    return abs(sm - sum(range(1,N+2)))