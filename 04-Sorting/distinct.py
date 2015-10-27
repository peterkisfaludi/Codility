# https://codility.com/demo/results/trainingZ97WM4-QCJ/

def solution(A):
    # write your code in Python 2.7
    return len(set(A))

"""
# https://codility.com/demo/results/training9GAWHG-YRK/

def solution(A):
    # write your code in Python 2.7
    N=len(A)
    if N==0:
        return 0
    
    A.sort()
    
    cnt=1
    prv=A[0]
    for x in A[1:]:
        if x!=prv:
            cnt+=1
        prv=x
    return cnt
"""