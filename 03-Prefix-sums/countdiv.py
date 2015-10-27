# https://codility.com/demo/results/trainingDM98X2-Z6H/

def solution(A, B, K):
    # write your code in Python 2.7
    
    F=(A//K)*K
    F=F if A%K==0 else F+K
    L=(B//K)*K
    
    if F<A or F>B or L<A or L>B or L<F:
        return 0
    
    return (L-F)//K+1