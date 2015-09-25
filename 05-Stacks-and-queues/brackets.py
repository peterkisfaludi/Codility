# https://codility.com/demo/results/trainingAGV2ZS-575/

def solution(S):
    # write your code in Python 2.7
    
    if len(S)==0:
        return 1
    stk = []
    
    for x in S:
        if x=='{' or x=='[' or x=='(':
            stk.append(x)
        else:
            if len(stk)>0:
                prv=stk[-1]
                if (x=='}' and prv=='{') or (x==']' and prv=='[') or (x==')' and prv=='('):
                    stk.pop()
                else:
                    return 0
            else:
                return 0
    if len(stk)!=0:
        return 0
    else:
        return 1
