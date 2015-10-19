# https://codility.com/demo/results/trainingDHC5VK-WQN/

def solution(S):
    # write your code in Python 2.7
    N=len(S)
    
    if N%2==0:
        return -1
        
    mid=N//2
    cnt=mid
    
    while cnt>0:
        if S[mid-cnt]!=S[mid+cnt]:
            return -1
        cnt-=1
            
    return mid