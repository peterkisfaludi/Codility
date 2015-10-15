# https://codility.com/demo/results/trainingVZV7SZ-8NM/

def solution(N):
    # write your code in Python 2.7
    
    s="{0:b}".format(N)
    
    cnt=0
    mx=0
    pv=-1
    for x in s:
        if x=='1':
            if pv=='0':
                mx=max(mx,cnt)
        else:
            if pv=='1':
                cnt=1
            else:
                if cnt>0:
                    cnt+=1
        pv=x                
    
    return mx