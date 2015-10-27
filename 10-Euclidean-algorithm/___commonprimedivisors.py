from math import sqrt
from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)
def solution(A, B):
    # write your code in Python 2.7
    
    cnt=0
    K=len(A)
    for k in range(K):
        if A[k]==B[k]:
            cnt+=1
        elif A[k]==1 or B[k]==1:
            continue
        else:
            s = int(max(sqrt(A[k]),sqrt(B[k])))
            passed=True
            for x in range(2,s+1):
                if (A[k]%x==0 and B[k]%x!=0) or (A[k]%x!=0 and B[k]%x==0):
                    passed=False
                    break
            if passed==True:
                cnt+=1
    return cnt