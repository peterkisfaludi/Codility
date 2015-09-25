# https://codility.com/demo/results/trainingA3K3DV-7EF/

def solution(X, A):
    # write your code in Python 2.7
    
    d=dict(zip(set(A),[0]*len(set(A))))
    cnt=0
    
    for k in range(len(A)):
        if d[A[k]]==0:
            d[A[k]]=1
            cnt+=1
            if cnt==X:
                return k
                
    return -1