# https://codility.com/demo/results/trainingQQ8QUT-CZR/

def solution(A):
    # write your code in Python 2.7
    
    N=len(A)
    A.sort()
    
    if N>6:
        A=A[0:3]+A[-3:]    
        N=6
    
    x,y,z=0,1,2
    m=A[0]*A[1]*A[2]
    
    while True:
        m=max(A[x]*A[y]*A[z],m)
        if z<N-1:
            z+=1
        elif y<N-2:
            y+=1
            z=y+1
        elif x<N-3:
            x+=1
            y=x+1
            z=y+1
        else:
            break
        
        
    return m