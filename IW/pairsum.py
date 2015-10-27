#Now, the second codility task I was faced with was a bit tougher. The goal was to create a function that, given a vector of integers A and an integer K, returned the number of integer pairs in the vector that, when added, sums up to K.
#Let me give you an example. Assume that you are given a vector A = [0, -1, 3, 2, -5, 7] and K = 2. Possible combinations to get K are (0, 2), (-1, 3), (3, -1), (2, 0),  (-5, 7), and (7, -5). In other words, the function should return 6.

def solution(A,K):
    N=len(A)
    
    cnt=0
    for x in range(N):
        for y in range(0,x) + range(x+1,N):
            print A[x], A[y], A[x]+A[y]
            if A[x]+A[y]==K:
                cnt+=1
    
    return cnt
    

sol= solution([0, -1, 3, 2, -5, 7],2)
print "SOLUTION"
print sol