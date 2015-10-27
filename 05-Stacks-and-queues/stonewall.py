# https://codility.com/demo/results/trainingJJHJFV-ZDR/

def solution(H):
    # write your code in Python 2.7
    
    stk=[]
    cnt=0
    
    for x in H:
        if len(stk)==0 or x>stk[-1]:
            cnt+=1
            stk.append(x)
        else:
            while True:
                if len(stk)==0:
                    stk.append(x)
                    cnt+=1
                    break
                
                a=stk[-1]
                if x<a:
                    stk.pop()
                elif x==a:
                    break
                else:
                    stk.append(x)
                    cnt+=1
                    break                                    
    return cnt
