# https://codility.com/demo/results/trainingQSG66P-62Q/

from collections import Counter
def solution(A):
    # write your code in Python 2.7
    
    cnt = Counter(A)
    for k,v in cnt.iteritems():
        if v%2!=0:
            return k