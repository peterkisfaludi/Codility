https://codility.com/demo/results/trainingZS9HDW-VWT/

def go(T):
    if T.l==None and T.r==None:
        return 0
    if T.l==None:
        return 1+go(T.r)
    if T.r==None:
        return 1+go(T.l)
    return 1+max(go(T.r),go(T.l))

def solution(T):
    # write your code in Python 2.7
    
    if T==None:
        return -1
    
    return go(T)