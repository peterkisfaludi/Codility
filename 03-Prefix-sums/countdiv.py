# https://codility.com/demo/results/training9MBBMJ-FCB/

def solution(A, B, K):
    # write your code in Python 2.7
    
    if A==B:
        if A%K==0:
            return 1
        else:
            return 0
            
    if K>B:
        return 0
    
    fst,lst=0,0
    
    lst = K*(B//K)
    fst = K*(A//K)
    if A%K!=0:
        fst+=K
        
    if fst>lst:
        return 0
    if lst==fst:
        return 1
        
    return (lst-fst)//K + 1