# https://codility.com/demo/results/training4H2TQD-9YX/

def solution(A):
    
    cntE=0
    cntT=0
    for x in A:
        if x==0:
            cntE+=1
        elif x==1:
            cntT+=cntE
            if cntT>1000000000:
                return -1

    return cntT