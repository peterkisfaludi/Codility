# https://codility.com/demo/results/trainingSYNSK7-XJ7/

def solution(S):
    # write your code in Python 2.7
    
    N=len(S)
    
    if N==0:
        return 1
        
    if N%2!=0:
        return 0
        
    cnt = 0
    
    for x in S:
        if x=='(':
            cnt+=1
        if x==')':
            cnt-=1
        if cnt < 0:
            return 0
            
    if cnt !=0:
        return 0
        
    return 1
