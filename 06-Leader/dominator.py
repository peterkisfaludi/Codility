# https://codility.com/demo/results/trainingSTQGEF-DGX/

def solution(A):
    # write your code in Python 2.7
    N=len(A)
    if N==0:
        return -1
    if N==1:
        return 0
    
    lead=A[0]
    cnt=1
    leadIdx=0
    
    for k in xrange(1,N):
        x=A[k]
        if cnt==0:
            lead=x
            leadIdx=k
            cnt=1
            continue
        
        if x!=lead:                
            if cnt==1:
                lead=None
            cnt-=1

        else:
            cnt+=1
        
    #print "fin",lead,cnt,leadIdx
    
    cnt=0
    for x in A:
        if x==lead:
            cnt+=1
    
    if cnt>N//2:
        return leadIdx
    else:
        return -1