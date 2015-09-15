def solution(X, Y, D):
    # write your code in Python 2.7    
    cnt= (Y-X)//D
    if (Y-X)%D!=0:
        return cnt+1
    return cnt