# https://codility.com/demo/results/trainingY68Y5K-HWS/

def solution(A):
    # write your code in Python 2.7
    
    N=len(A)
    if N<=1: return 0
    
    profit=0
    maxProfit=0
    startPrice = A[0]
    
    for x in A[1:]:
        
        profit = max(profit, x - startPrice)
        startPrice = min(x,startPrice)
        if startPrice==x:
            profit=0
        maxProfit = max(maxProfit,profit)        

    if maxProfit < 0:
        return 0
    return maxProfit