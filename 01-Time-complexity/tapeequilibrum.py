def solution(A):
    # write your code in Python 2.7
    sm=sum(A)
    lsm = 0
    rsm = sm
    minsm = -1
    
    for x in A[:-1]:
        lsm+=x
        rsm-=x
        
        if minsm==-1:
            minsm = abs(lsm - rsm)
        else:
            minsm = min(minsm,abs(lsm-rsm))
            
    return minsm