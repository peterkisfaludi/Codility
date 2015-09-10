def solution(H):
    # write your code in Python 2.7
    
    N=len(H)
        
    cnt=0
    if N==1:
        return 1
        
    stck = [H[0]]
    cnt=1
        
    for x in H:                
        v=stck[-1]
        if x > v: 
            cnt+=1
            stck.append(x)
            continue
        elif x == v:
            continue
        else:
            while len(stck)>0:
                v=stck[-1]
                if x<v:
                    stck.pop()
                elif x==v:
                    break
                else:
                    cnt+=1
                    stck.append(x)
        if len(stck)==0:
            cnt+=1
            stck.append(x)            
                
    return cnt
