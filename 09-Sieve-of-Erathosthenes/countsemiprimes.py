https://codility.com/demo/results/trainingR86XNN-FNW/

def solution(N, P, Q):
    # write your code in Python 2.7
    M=len(P)
    #primes   
    R = [True] * (N+1)
    R[0]=False
    R[1]=False
    
    x=2
    while x*x <= N:
        if R[x]==True:
            y=x*x
            while y<=N:
                R[y]=False
                y+=x
        x+=1

    pm=[i for (i,x) in enumerate(R) if x==True]
    
    S = [False] * (N+1)
    for x in pm:
        if x*x > N:
            break
        
        for y in pm:
            if x*y > N:
                break
            S[x*y]=True
            
    cn = [0]*(N+1)    
    cnt=0
    for x in range(N+1):        
        if S[x]==True:            
            cnt+=1
        cn[x]=cnt
                
    ret=[]
    for x in range(M):
        p=P[x]
        q=Q[x]
        
        if (p<4 and q<4) or (p>N and q>N):
            ret.append(0)
            continue
        
        if P<4:
            p=4
        if q<4:
            q=4
        if p>N:
            p=N
        if q>N:
            q=N
            
        nm = cn[q]-cn[p]
        if S[p]==True:
            nm+=1
        ret.append(nm)
            
        
        
                
    return ret 