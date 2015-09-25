# https://codility.com/demo/results/training4TPBAD-ZMX/

def solution(A, B):
    # write your code in Python 2.7
    
    N=len(A)
        
    cnt=N
    stk=[]
    
    for x in range(N):
        s=A[x]
        d=B[x]
        
        
        if d==1:
            stk.append(s)
        else:
            while len(stk)>0:
                cnt-=1
                es = stk[-1]
                if es>s:                    
                    break
                else:
                    stk.pop()
                    
    return cnt
