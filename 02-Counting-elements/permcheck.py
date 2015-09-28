# https://codility.com/demo/results/trainingAFY6Z9-NF2/

def solution(A):
    # write your code in Python 2.7
    N=len(A)
    
    d=dict(zip(range(1,N+1),[0]*N))
    
    cnt=0
    for x in A:
        try:
            if d[x]==0:
                d[x]=1
                cnt+=1
            else:
                return 0
        except:
            return 0
            
    if cnt==N:
        return 1
    return 0